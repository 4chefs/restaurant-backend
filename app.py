from flask import Flask
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app, template_file='swagger.yaml')

if __name__ == "__main__":
    app.run(debug=True)
