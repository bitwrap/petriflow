import petriflow

import examples.counter
import examples.pointer

# Counter model supports n++/n-- operations on a 2-n vector
Counter = petriflow.Model('counter_v1', examples.counter.v1)

# Pointer models create/update/disable operations on a named 'object'
Pointer = petriflow.Model('pointer_v1', examples.pointer.v1)
