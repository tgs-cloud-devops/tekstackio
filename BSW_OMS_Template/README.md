# Create a OMS configuration on Azure

<a href="https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fkurtcrowley%2Ftekstackio%2Fmaster%2FBSW_OMS_Template%2Ftemplate.json" target="_blank">
    <img src="http://azuredeploy.net/deploybutton.png"/>
</a>
<a href="http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2Fkurtcrowley%2Ftekstackio%2Fmaster%2FBSW_OMS_Template%2Ftemplate.json" target="_blank">
    <img src="http://armviz.io/visualizebutton.png"/>
</a>

## Notable Variables

|Name|Description|
|:---|:---------------------|
|virtualNetworkName|Name of the Virtual Network|
|adPDCVMName|The name of the Primary Domain Controller|
|adBDCVMName|The name of the Backup\Second Domain Controller|
|sqlVMName|The prefix for the SQL VM Names|
|sqlwVMName|The name of the File Share Witness|
|spwebVMName|The Prefix of the SharePoint Web Server VMs|
|spappVMName|The Prefix of the SharePoint App Server VMs|
|windowsImagePublisher|The name of the pulisher of the AD and Witness Image|
|windowsImageOffer|The Offer Name for the Image used by AD and Witness VMs|
|windowsImageSKU|The Image SKU for the AD and Witness Image|
|sqlImagePublisher|The name of the pulisher of the SQL Image|
|sqlImageOffer|The Offer Name for the Image used by SQL|
|sqlImageSKU|The Image SKU for the SQL Image|
|spImagePublisher|The name of the pulisher of the SharePoint Image|
|spImageOffer|The Offer Name for the Image used by SharePoint|
|spImageSKU|The Image SKU for the SharePoint Image|
|windowsDiskSize|The size of the VHD allocated for AD and Witness VMs Data Disk|
|sqlDiskSize|The size of the the VHD allocated for SQL VMs Data and Log Disks|
|spDiskSize|The size of the VHD allocated for the SP VMs Data Disk|
