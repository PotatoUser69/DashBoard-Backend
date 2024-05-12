Base Skeleton to start your application using Flask-AppBuilder
--------------------------------------------------------------

- Install it::

	pip install -r requirements.txt

- Run it::

	# Go into project
	$ cd AutoChartBackend
	# Run api
	$ pyhton api.py

That's it!!

The server is running in the port 5000

- API endpoint's::

	/datasets
        	return a list of all CSV datasets in the folder data
	/chart/<string:chart>
        	return the name of the main and secondary chart choosen by the programme
    	/htmlread/<string:file>
        	return the HTML file to the front-end to be displayed
