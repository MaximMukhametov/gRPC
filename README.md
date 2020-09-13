<p align="center">
<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcSrKJpP7aFWyCoQGBmfuBHSLCtukAPGsHAlfw&usqp=CAU" alt="drawing" width="400"/>
</p>

#### A small project of client-server communication between Go and Python code using the [gRPC](https://grpc.io/ "A high-performance, open source universal RPC framework") framework 

Enter the following command to clone repository and create environments and start python grpc-server :
```bash
git clone git@github.com:MaximMukhametov/gRPC.git \
&& cd gRPC && python3 -m venv venv && source venv/bin/activate \
&& pip install -r python/requirements.txt \
&& python python/server.py
```


Then you can open another terminal in the same directory 
(do not forget to activate the virtual environment)
run the following commands:

To run python client:
```bash
python python/client.py
```

To run golang client:
```bash
go run golang/client/main.go
```
