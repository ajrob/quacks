import reflex as rx

class ReflexquackConfig(rx.Config):
    pass

config = ReflexquackConfig(
    app_name="reflex_quack",
    api_url="https://quacks.onrender.com:8000",
    deploy_url="http://quacks.onrender.com:3000"
)
