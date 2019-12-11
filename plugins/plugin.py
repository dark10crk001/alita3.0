import importlib

class Plugin:
    def __init__(self):
        pass
    
    def exec(self,cmd,keywords):
        module = 'plugins.weather'
        func_name = 'exec'
        m = importlib.import_module(module)
        print(m)
        func = getattr(m, func_name)

        print("plugin execute:",cmd,keywords)
        return func(cmd,keywords)


if __name__ == "__main__":
    p = Plugin()
    p.exec("cmd:weather",["北京","天气","查看"])