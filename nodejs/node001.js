var http = require('http');
var events = require('events')

var eventEmiter = new events.EventEmitter();

//创建事件处理程序
var connectHandler = function connected(){
    console.log('连接成功');
    eventEmiter.emit('data_received');
}


eventEmiter.on('connection', connectHandler)

eventEmiter.on('data_received', function(){
    console.log('数据接收成功');
})

eventEmiter.emit('connection');
console.log('程序执行完毕');

var buf = Buffer.alloc(20, "www.runoob.com");
//var buf =  Buffer.alloc("www.runoob.com");
var json = buf.toJSON(buf);
console.log(json)



/*
http.createServer(function (request, response) {

	// 发送 HTTP 头部
	// HTTP 状态值: 200 : OK
	// 内容类型: text/plain
	response.writeHead(200, {'Content-Type': 'text/plain'});

	// 发送响应数据 "Hello World"
	response.end('Hello World\n');
}).listen(8888);

// 终端打印如下信息
console.log('Server running at http://127.0.0.1:8888/');

*/
