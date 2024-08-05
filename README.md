This is a basic docker-compose stack for scraping runtime metrics from the schedd.

## Configuration

Run ./configure, which takes the following key-value pairs:
`time <integer>`: Sets the time interval for prometheus to scrape, and for polling to occur
`path <string>`: Sets the filepath to read from and write to for prometheus
`poll <true|false>`: Determines whether or not to run condor_diagnostics in the background

## Startup

Make sure you have your condor environment configured and that the `htcondor` package is in your python installation.

Run `./start` after configuration; you will be prompted for the sudo password in order to start your containers. 

By default Grafana will be on localhost:3000, Prometheus on localhost:9090, and the webserver on localhost:5000, but you can of course configure these in `docker-compose.yml`.

Type Ctrl-C in the shell to exit the process.