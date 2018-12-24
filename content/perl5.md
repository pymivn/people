# Perl 5 cho người lười

 $ whatis -s1 perl
 perl (1)             - The Perl 5 language interpreter
 $ whatis -s1 cpan
 cpan (1)             - easily interact with CPAN from the command line

perl -e
perldoc perlintro


Like bash
String double quote will substitue var
String single quote keep verbatim

End with ;

Variable define: my x = 10;
my y = 20;
print $x + $y - 2 * 10 / 2;
print 5 != 4 && 2 < 5 || !(3 > 5)
print "meo" ne "cho"

different number and comparision because variable has no type

print hello world: 4 MB RAM


$_


## Array - similar to Python list
my @names = ("chim", "meo", "ga", 42); # diff types
print($names[0]);

$#names  -> index of last elemen (like python[-1])

@names return number when do number operators:

@names + 5

Multiple index access
@names[1, 3]

Slice
@names[1..3]

sort @names
reverse @names

@ARGV @_
## Hash (key-value pairs) - smilar to Python dicto

```perl
my %phonebook = (
    HVN => "khong co so",
    PyMi => 0909090909,
);
print($phonebook{"HVN"})
print($phonebook{"khong ton tai"})
```

or
```
my $pymiers = {
    HVN => {
        address => "VietNam",
        homepage => "www.familug.org",
    }
}

print "Homepage is $pymier->{'HVN'}->{'homepage'}
```


## Control flow

if ( condition ) {
    ...
} elsif ( other condition1 ) {
    ...
} elsif ( other condition2 ) {
    ...
} else {
    ..
}

unless ( ... ) = if not something


while ( condition ) {
    ...
}
until ( condition ) {
    ...
}

while ( 1 ) {
    print "HELLO PyMI.vn"
}

for EXACTLY like C
for ($i = 0; $i <= 10; $i++) {
}


lovely foreach

```
foreach (@name) {
    print "Hello $_ \n"
}
```

OR

```
foreach my $key (keys %phonebook) {
    print "Value of $key is $phonebook{$key} \n"
}
```

## IO
open(my $in, "<", "input.txt")
open(my $out, ">", "input.txt")
open(my $appendout, ">>", "input.txt")

while $(<$in>) {
    print "Just read in this line $_";
}

close($in)
close($out)
close($appendout)


## Regex
    THE MOST FAMOUS, POPULAR, probably BEST THING IN PERL

my $phone = "0990009990";
if ($phone =~ /[0-9]{10,11}/) {
    print "Good phone number";
} else {
    print "Seem bad phone number";
}

print("Perl is good" =~ s/g/for f/)

```
perl -e 'my $words = "Perl is good";
print $word;
$words =~ s/g/for f/g;
print "$words \n"'
# Perl is for food
```

## Subroutine
Similar function in other lang


sub double {
my $x = shift;
return $x * 2;
}

print double(21);

sub sumtwo {
my ($first, $second) = @_;
return $first + $second
}
print sumtwo(2,3);


## Using module

use something

 use strict;
 use warnings;


## Sample program

```
#!/usr/bin/perl
use strict;
use warnings;
use IO::Handle;

my ( $remaining, $total );

$remaining = $total = shift(@ARGV);

STDOUT->autoflush(1);

while ( $remaining ) {
    printf ( "Remaining %s/%s \r", $remaining--, $total );
    sleep 1;
}

print "\n";
```

Thay sed
```
$ perl -i.bak -lp -e 's/Bob/Robert/g' *.txt
```

https://en.wikipedia.org/wiki/Perl

https://www.perl.org/

25000 package on CPAN
vs Python 162,637 projects as of 2018 Dec 24.

https://github.com/kaxap/arl/blob/master/README-Perl.md

https://github.com/brendangregg/FlameGraph/blob/90533539b75400297092f973163b8a7b067c66d3/dev/hcstackcollapse.pl
https://github.com/so-fancy/diff-so-fancy/blob/5c96bddd5b53df4171cb3ebc1a2e1e16f0611806/diff-so-fancy
https://github.com/mojolicious/mojo/blob/master/lib/Mojo/IOLoop/Server.pm
