#create a script that replaces a misspelling in a file.
exec { 'sed':
  command => "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
  path    => ['/bin/', '/sbin/', '/usr/bin/', '/usr/sbin/'],
}