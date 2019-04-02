// Import module hello
var addon = require('bindings')('hello');

// call function hellox
console.log(addon.hellox()); // 'world'