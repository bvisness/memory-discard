// Basically wat2wasm using the SpiderMonkey shell.
// Call like:
//   js build-sm.js input.wat output.wasm
const text = os.file.readFile(scriptArgs[0]);
const bytes = wasmTextToBinary(text);
os.file.writeTypedArrayToFile(scriptArgs[1], bytes);
