<?php
function isMobile(){
	return preg_match("/(android|avantgo|blackberry|bolt|boost|cricket|docomo|fone|hiptop|mini|mobi|palm|phone|pie|tablet|up\.browser|up\.link|webos|wos)/i", $_SERVER["HTTP_USER_AGENT"]);
}
	
if (isMobile()){
	echo "<h1>Yes, Mobile phone detected</h1>";
} else {
	echo "<h1>No, Desktop detected</h1>";
}
?>