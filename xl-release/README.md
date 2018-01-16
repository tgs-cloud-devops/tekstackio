# BCBSA XL Release Configuration

## XL Release directory structure 

The *xl-release-7.2.0-server.zip* file contains the entire XL release installation including all the configuration files and the custom extensions TEK implemented for BCBSA. 

The following directory structure exists in the installation directory: 

 - **archive**: Embedded archive / reporting database 
 - **bin**: Server startup scripts 
 - **conf**: Configuration files 
 - **ext**: XL Release extensions implemented for BCBSA 
 - **hotfix**: Contains hotfixes that correct issues with the server software 
 - **lib**: Binary libraries 
 - **log**: Server log files 
 - **plugins**: XL Release extensions that are packaged as plugins 
 - **repository**: Embedded XL Release database 

Henceforth the installation directory is referred to as **XL_RELEASE_SERVER_HOME**. 

The following directory structure exists in the XL_RELEASE_SERVER_HOME/ext directory: 

 - **synthetic.xml**: Tile configuration file. Defines properties for all tile elements. Each tile has a section defined in this file. The properties are parameters that can be set for each tile by clicking on the configure button in the release dashboard view. To reflect any changes done, the XL Release service must be restarted. 
 - **acme**: Contains several tile extension examples. 
 - **bcbsa**: Contains all the custom tile server-side Jython scripts. Each one matches a corresponding .html view template file. 
 - **web**: Contains all the .html templates for the tile and details views. 
	 - **acme**: .html template examples 
	 - **bcbsa**: custom .html templates implemented for BCBSA 

 
## Change lifecycle 

 - **Updating the synthetic.xml file**: after updating the file, the XL Release service must be restarted. 
	 - sudo service xl-release stop 
	 - sudo service xl-release start 
 - **Updating the tile .html code**: when updating the tile or tile detail .html code, the updates can be immediately seen by refreshing the corresponding XLR tile page. 
 - **Creating a new tile**:  
	 - Create a new server-side script file. 
	 - Create new html template files. 
	 - Add a Tile configuration section to synthetic.xml. 
	 - Restart the XL Release service. 
 - **Create new BCBSA release**: 
	 - Click on design/folders, select BCBSA-POC. 
	 - Copy a previous release (example: 2017 Release 4) 
	 - Change the name to the new release name. 
	 - Select the release, then click on Release flow selection box. 
	 - Select variables, then adjust the variable entries accordingly.  

## Special instructions 

 - **Running the xlr-data-webservice**: This service is utilized to test data transporting and currently provides a temporary bridge to get the selenium results to XL Release. 
	 - Go to the xlr-data-webservice directory/Python2.7/app directory 
	 - Execute the webservice: Sudo Python main.py 
