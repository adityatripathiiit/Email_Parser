<?php
// Same as error_reporting(E_ALL);
//ini_set('error_reporting', E_ALL);
ini_set('memory_limit', '850M');
set_time_limit(0);
 
function scrap_drush_command()
{
    $items = array();
    $items['scrap_email'] = array(
        'description' => "Scraps all emails from google archive(.mbox) and stores it in output-email.csv in current dir",
        'arguments' => array(//            'type' => 'The type of the smile (half_moon, polity, etc.)',
        ),
        'options' => array(
            'file-name' => 'path to name of the google archive file(.mbox). It can be relative to current dir',
        ),
        'examples' => array(
            'drush scrap_email --file-name=my-gmail.blox' => 'scraps all emails from my-gmail.mbox and stores emails in output-emails.csv in current dir',
        ),
        'aliases' => array('semail'),
        'bootstrap' => DRUSH_BOOTSTRAP_DRUSH, // No bootstrap at all.
    );
    return $items;
}
 
function drush_scrap_email()
{
    $filepath = drush_get_option('file-name');
    if (!file_exists($filepath)) {
        $filepath = getcwd() . '/' . $filepath;
        if (!file_exists($filepath)) {
            drush_die('File - ' . $filepath . ' doesn\'t exist', 0);
        }
    }
 
   drush_log('begin scraping...','ok');
 
    $chunk = 10 * 1024 * 1024; // bytes per chunk (10 MB)
 
    $f = fopen($filepath, 'rb') or die("Couldn't get handle for " . $filepath);
    $data = '';
    if ($f) {
        while (!@feof($f)) {
            $data .= fgets($f, 4096);
        }
        fclose($f);
    }
 
    drush_log('done reading string of size: ' . mb_strlen($data, '8bit') . '... start searching','ok');
 
    $pattern = "/([a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9._-]+)/";
    preg_match_all($pattern, $data, $matches);
 
    $all_emails = array_unique(array_values($matches[0]));
    $all_emails_filtered = array_filter($all_emails, 'filter_bad_emails');
 
    print_r($all_emails_filtered);
    drush_log('Count:' . count($all_emails_filtered),'ok');
 
    drush_log('writing...','ok');
 
    $date = date('m-j-y');
    $filename = 'output-emails-'.$date.'.csv';
    $filepath = getcwd() . '/' . $filename;
 
    $file = fopen($filepath, "w") or die("Couldn't get handle for " . $filepath);
    if ($file) {
        foreach($all_emails_filtered as $email){
            fputcsv($file, array($email));
        }
    }
 
    fclose($file);
    drush_print('done');
}
 
function filter_bad_emails($email)
{
    $char = $email[0];
    $email_tokens = explode('@', $email);
    $domain_name = array_pop($email_tokens);
    $ext_tokens = explode('.', $domain_name);
    $ext = array_pop($ext_tokens);
    if ($char == '-' || $char == '_' || $char == '.' || is_numeric($char) || (strlen($email) > 30) || (strlen($ext) > 4) || is_numeric($ext) || ($ext == 'c') || ($ext == 'n') || ($domain_name == 'mail.gmail.com')) {
        return false;
    } else {
        return true;
    }
}