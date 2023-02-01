(module
    (memory (export "memory") 32768) ;; 2GiB
    (func (export "touch") (param $base i32) (param $length i32)
        (memory.fill (local.get $base) (i32.const 1) (local.get $length))
    )
    (func (export "discard") (param $base i32) (param $length i32)
        (memory.discard (local.get $base) (local.get $length))
    )
)
