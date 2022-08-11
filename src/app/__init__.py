from flask import Flask

def create_app():
    app = Flask(__name__)
    
    from app.views import main_views, auth_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(auth_views.bp)

    return app

app = create_app()
    
if __name__ == '__main__':
    app.run()