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

test('test', samscpp)