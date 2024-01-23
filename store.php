<?php
if (isset($_GET["SSID"]))
{
	//$ssid=$_POST["SSID"];
        $ssid=$_GET["SSID"];
        $command = escapeshellcmd('python3 /var/www/html/test.py '.$ssid);
        $output = exec($command);
        echo $output;
        
	//$password=1;
        //exec("ifconfig eth0 2>&1",$output,$return);
        //echo $ssid
        //exec("/var/www/html/reboot1.sh"); . $hello
        //exec("sudo python3 /var/www/html/test.py" .$ssid);
        
        //$result = shell_exec("sudo python3 /var/www/html/test.py" .$ssid);
        //echo $result
        //echo $ssid);
        //exec("/var/www/html/reboot1.sh")
        //echo $output[0];
        //echo $return;
        //var_dump($return);
        //echo "return is : $return" . "\n";
        //var_dump($output);
        if($return !=0) {
           echo "<br />";
           echo "Failed to update APN";
           echo '<a href="Wlan.html"><br /><br />Return to Previous Page</a>';
        }else{
           echo "<br />";
           echo "<br />";
           echo "Sucessfully updated APN";
           echo '<a href="Wlan.html"><br /><br />Return to Modem Setup Page</a>';
        }
        //echo "<a href="Wlan.html">Click here</a>";
        //$myFile = "/etc/wpa_supplicant/wpa_supplicant.conf";
	//$fh = fopen($myFile, 'a') or die("can't open file");
	//$stringData = "network={\n\tssid=\"".$ssid."\"\n\tpsk=\"".$password."\"\n\tkey-mgmt=WPA-PSK\n}";
	//fwrite($fh,"\n");
	//fwrite($fh, $stringData);
	//fwrite($fh,"\r\n");
	//fclose($fh);
        //echo "successfully connected to $ssid";
        // echo <a href="Wlan.html">Click here</a>
} ?>

