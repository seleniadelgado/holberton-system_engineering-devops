#create a script that replaces a misspelling in a file.
exec { 'sed':
     command => 'sed -i 's/phpp/php/g' wp-settings.php
     path    => ['/var/www/html']
}