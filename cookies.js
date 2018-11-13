module.exports {
	
	var cookies = {
		AWSALB: "AWSALB",
		GSESSIONID: "GSESSIONID",
		cass: 2,
		gdId: "gdId"
	}

	function setCookie(AWSALB, GSESSIONID, cass, gdId) {
		cookies.AWSALB = AWSALB;
		cookies.GSESSIONID = GSESSIONID;
		cookies.cass = cass;
		cookies.gdId = gdId;
	}

}