(module
    (memory (export "memory") i64 32768) ;; 2GiB
    (func (export "fill") (param $base i64) (param $length i64)
        (memory.fill (local.get $base) (i32.const 1) (local.get $length))
    )
    (func (export "check") (param $base i64) (param $length i64) (result i64)
        (local $i i64)
        (local $res i64)

        (loop $checkLoop
            (local.set $res (i64.or ;; or the result with the current num
                (local.get $res)
                (i64.load (i64.add (local.get $base) (local.get $i)))
            ))

            (local.set $i (i64.add (local.get $i) (i64.const 8))) ;; increment $i
            (br_if $checkLoop (i64.lt_u (local.get $i) (local.get $length))) ;; back to beginning
        )

        (return (local.get $res))
    )
    (func (export "discard") (param $base i64) (param $length i64)
        (memory.discard (local.get $base) (local.get $length))
    )
)
