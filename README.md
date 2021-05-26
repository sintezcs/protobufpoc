# Google Protobuf serialization POC

This script uses Google Protobuf library to serialize fake events, similar to 
notification events that we receive from stream.io. The script calculates an average 
message size for serialized messages (comparing to regular json serialization). 
The average protobuf-serialized message is ~32% smaller than json-serialized. 

### Building protobuf python classes

1. Install protobuf on MacOS:\
`brew install protobuf`
2. Generate python code (run in the project dir):\
`protoc --python_out=. notification.proto`

### Running the project
1. Install dependencies:\
`python3 -m venv .env && source .env/bin/activate && pip install -r requirements.txt`
2. Run the script:\
`python3 main.py`
