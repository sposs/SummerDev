#!/usr/bin/perl -w

$x = 1;
$y = 1;
$z = 1;
$len = sqrt($x**2 + $y**2 + $z**2);
$comp = sqrt(3);

print ("par la racine : $len\npar le calcul : $comp\n");

my @a;
my $a;
my @b;
my $b;

if (defined($a))
{
	print "scalar a : $a\n";
}

if ($a==0)
{
	print "scalar a : $a\n";
}

if (defined($b))
{
	print "scalar b : $b\n";
}

if (defined(@a))
{
	print "list a : @a\n";
}

if (defined(@b))
{
	print "list b : @b\n";
}
$a = 0;

if (defined($a))
{
	print "(0) scalar a : $a\n";
}

if ($a==0)
{
	print "(a=0) scalar a : $a\n";
}

