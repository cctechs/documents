var Hello = require('./hello');
hello = new Hello();
hello.setName('123');
hello.sayHello();


function say(world){
    console.log(world);
}

function fnExec(cbFunc, value){
    cbFunc(value);
}

var t = setTimeout(() => {
    console.log('timeout');
}, 2000);
fnExec(say, 'qwe')
clearTimeout(t);
console.log(__filename)
console.log(__dirname)


process.on('exit', function(code){
    console.log(code);
});
console.log('程序退出');

console.error(process.execPath);
console.error(process.platform);