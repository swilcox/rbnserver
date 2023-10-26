# RBN Server

## Overview

This is a quick Django sample project to test out some things I've not used before.

Purpose is to store [Reverse Beacon Network](https://reversebeacon.net) spots in a database and be able to query those spots.

## Goals of this sample project
* [x] try out Django Ninja as a DRF alternative
* [x] try out Dramatiq as a celery alternative

## Future Tasks
* [ ] django channels for websocket client connections
* [ ] a computed band field based on frequency
* [ ] auth / security

## Slightly more detail:

In order to exercise the Dramatiq library, adding a new spot record triggers a Dramatiq background task (the "actor") to actually perform the add.

The order of execution would be:
- post to `/api/spots/`.
- task is queued via Dramatiq (redis backend).
- initial response is given to the request so the client can be done.
- dramatiq worker process picks up the task and actually performs the record add.

## Installation and setup

### Requirements
* python and pdm
* postgres (though could be configured for other databases)
* redis (though rabbitmq is also an option)
* rbnread client (see other project)
* preferably have your ham radio license

Using pdm for this project.

*TODO:* more instructions here.
