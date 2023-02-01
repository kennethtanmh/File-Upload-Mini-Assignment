from flask import Flask, request
from flask_restful import Resource, Api
import os

app = Flask(__name__)
api = Api(app)

class FileUpload(Resource):
    def post(self):
        files = request.files.getlist("files")
        filenames = []
        for file in files:
            file.save(os.path.join("/home/coga/Desktop/pass/backend/uploads", file.filename))
            filenames.append(file.filename)
        return {"message": "Files uploaded successfully", "filenames": filenames}

api.add_resource(FileUpload, '/api/upload')

if __name__ == '__main__':
    app.run(debug=True, port=5000)