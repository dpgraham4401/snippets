project('samscpp', 'cpp',
        version : '1.0.0',
        default_options : ['warning_level=3', 'cpp_std=c++20'])

samscpp = executable('samscpp', 'main.cpp', install : true)

# Lesson 3
types = executable('types', 'lesson3/types.cpp', install : true)

# Lesson 4
arrays = executable('arrays', 'lesson4/arrays.cpp', install : true)
strings = executable('strings', 'lesson4/strings.cpp', install : true)

# Lesson 5
arrays = executable('ops', 'lesson5/operators.cpp', install : true)

# lesson 6
conditions = executable('conditions', 'lesson6/conditions.cpp', install: true)

# lesson 7
fns = executable('fns', 'lesson7/fns.cpp', install: true)


# lesson 8
fns = executable('point', 'lesson8/pointers.cpp', install: true)

test('test', samscpp)
