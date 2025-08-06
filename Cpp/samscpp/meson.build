project('samscpp', 'cpp',
        version : '1.0.0',
        default_options : ['warning_level=3', 'cpp_std=c++20'])

samscpp = executable('samscpp', 'main.cpp', install : true)

types = executable('types', 'lesson3/types.cpp', install : true)


arrays = executable('arrays', 'lesson4/arrays.cpp', install : true)

test('test', samscpp)