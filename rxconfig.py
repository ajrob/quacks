import reflex as rx

class ReflexquackConfig(rx.Config):
    pass

config = ReflexquackConfig(
    app_name="reflex_quack",
    #api_url="https://quacks.onrender.com",
    api_url="http://192.168.0.168:8000",
    deploy_url="http://192.168.0.168:3000"
)
