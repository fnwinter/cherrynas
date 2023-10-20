import reflex as rx

config = rx.Config(
    app_name="cherrynas",
    db_url="sqlite:///pynecone.db",
    env=rx.Env.DEV,
)
