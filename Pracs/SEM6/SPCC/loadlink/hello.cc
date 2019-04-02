#include <napi.h>

// Napi => Node-API
// Napi::String, defines Syting for node
// Method has a return type of node string
// Method is passed the current environment as Napi::CallbackInfo& which is again predefined
// Get current environment from info.Env()
// return new Node String, with current env and value as "world"
Napi::String Method(const Napi::CallbackInfo& info) {
  Napi::Env env = info.Env();
  return Napi::String::New(env, "world");
}


// Create a function Init, which returns Node object, and takes current env and an exports object
// Set Node string hellox to Node function Method
Napi::Object Init(Napi::Env env, Napi::Object exports) {
  exports.Set(Napi::String::New(env, "hellox"),
              Napi::Function::New(env, Method));
  return exports;
}

// Create node_api_module called hello, with init function inside
NODE_API_MODULE(hello, Init)