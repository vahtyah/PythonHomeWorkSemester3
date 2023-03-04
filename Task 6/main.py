def main(*r):
    s = ({'PERL6', 1989, 1992, 1962},
         {'PERL6', 1989, 1992, 1976},
         {'PERL6', 1989, 2005, 1962},
         {'PERL6', 1989, 2005, 1976},
         {'PERL6', 1989, 2010, 'C++'},
         {'PERL6', 1989, 2010, 'NINJA'},
         {'PERL6', 1989, 2010, 'CSV'},
         {'PERL6', 1991, 'C++', 1962},
         {'PERL6', 1991, 'C++', 1976},
         {'PERL6', 1991, 'NINJA'},
         {'PERL6', 1991, 'CSV'},
         {'PERL6', 2017},
         {'CUDA'},
         {'SLIM'})
    s1 = set(*r)
    return [i for i in range(len(s))
            if not (len(s[i] - s1))][0]


print(main([1989, 2005, 'CUDA', 'C++', 1976]))
print(main([1989, 1992, 'PERL6', 'NINJA', 1962]))
print(main([1991, 2005, 'PERL6', 'C++', 1962]))
print(main([2017, 2010, 'SLIM', 'CSV', 1976]))
print(main([2017, 2010, 'PERL6', 'CSV', 1962]))