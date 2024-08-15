# Creating manifest to fix file name typo
exec { 'fix_typo':
  command => '/bin/mv /var/www/html/wp-includes/class-wp-locale.php /var/www/html/wp-includes/class-wp-locale.phpp',
  onlyif  => '/bin/test -f /var/www/html/wp-includes/class-wp-locale.php',
}
