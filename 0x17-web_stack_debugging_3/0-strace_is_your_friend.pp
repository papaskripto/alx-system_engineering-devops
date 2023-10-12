# Fix Apache server internal error
exec { 'fix 500 error':
  onlyif  => 't -e /var/www/html/wp-settings.php,
  command => 'sed -i 's/phpp/php/' /var/www/html/wp-settings.php',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'
}
