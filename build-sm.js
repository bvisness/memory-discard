// Basically wat2wasm using the SpiderMonkey shell.
// Call like:
//   js --wasm-memory-control build-sm.js input.wat output.wasm
const text = os.file.readFile(scriptArgs[0]);
const bytes = wasmTextToBinary(text);
if (!WebAssembly.validate(bytes)) {
    throw `${scriptArgs[0]} was not a valid WASM module.`;
}
os.file.writeTypedArrayToFile(scriptArgs[1], bytes);
