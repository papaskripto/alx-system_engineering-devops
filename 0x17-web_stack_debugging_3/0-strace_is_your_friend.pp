# Fix Apache server internal error
exec { 'fix 500 error':
  command => 'sed -i 's/class-wp-locale.phpp/class-wp-locale.php/g' /var/www/h\
tml/wp-settings.php',
  path    => '/bin'
}
