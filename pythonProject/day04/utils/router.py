class DemoRouter(object):
    def db_for_read(self,model,**hints):
        print("read")
        print(model._meta.model_name)
        return 'bak'

    def db_for_write(self,model,**hints):
        print('write')
        return 'default'