// 导入 CryptoJS 库
var CryptoJS = require("crypto-js");

// 定义字符串
var str = "yytkjfgzmnklfgyy";

// 使用 CryptoJS 的 enc.Utf8.parse 方法将字符串转换为 WordArray 对象
var wordArray = CryptoJS.enc.Utf8.parse(str);

// 打印 WordArray 对象
console.log(wordArray);
