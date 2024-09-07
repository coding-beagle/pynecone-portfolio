import pynecone as pc

class PyneportfolioConfig(pc.Config):
    pass

config = PyneportfolioConfig(
    app_name="pyne_portfolio",
    db_url="sqlite:///pynecone.db",
    env=pc.Env.DEV,
)