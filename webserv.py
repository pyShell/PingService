import tornado.ioloop
import tornado.web
import pingservice as ps
import pingdb
import time


config_file = 'ping_config'
file_data = [x for x in open(config_file, 'r').readline().split()]


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        data = (x for x in pingdb.DatabaseHandler().get_values() 
                if x['time'] > (time.time() - 3600))
        self.render('template.html', title='PingService', 
                    file_info=file_data, db_info=data)


application = tornado.web.Application([(r'/', MainHandler), ])

if __name__ == '__main__':
    ps.PingService(file_data).start()
    application.listen(80)
    tornado.ioloop.IOLoop.instance().start()
