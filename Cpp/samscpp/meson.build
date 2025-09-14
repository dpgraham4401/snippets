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
conditions = executable('conditions', 'lesson6/conditions.cpp', install : true)

# lesson 7
fns = executable('fns', 'lesson7/fns.cpp', install : true)

# lesson 8
fns = executable('point', 'lesson8/pointers.cpp', install : true)

# lesson 9
cls = executable('cls', 'lesson9/classes_obj.cpp', install : true)
structs = executable('structs', 'lesson9/cpp_structs.cpp', install : true)

# lesson 10
inheritance = executable('inheritance', 'lesson10/inheritance.cpp', install : true)

# lesson 11
poly = executable('poly', 'lesson11/polymorphism.cpp', install : true)
abc = executable('abc', 'lesson11/abc.cpp', install : true)

# lesson 14
macros = executable('macros', 'lesson14/macros.cpp', install : true)

# lesson 15
stdlibtemps = executable('stdlibtemps', 'lesson15/std_temp_lib.cpp', install : true)


test('test', samscpp)
