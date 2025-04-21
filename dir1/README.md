# apiContent 

Services repository for content related business logic

* [Jenkins Pipeline Job](https://pipeline.domo.com/job/_pipelines/job/apiContent/job/master/)
* [Swagger Docs](https://git.empdev.domo.com/pages/Services/api-registry/?urls.primaryName=apiContent)

## IntelliJ Plugin Dependencies 
* run "gradlew idea" to enable Annotation Processing
* Install the Lombok Plugin for Intellij

## DomoRigs
* Create a lease ```tug-eks create lease -t domo/brief/master/dev-apicontent```
* Pin a service to a specific version ```tug-eks set ns-var -g apicontent -p Deployment -n version -l "1.0.14868_master"```
* Unpin service ```tug delete var -g apicontent -u NULL -p Deployment -c NULL -k version```
* List pods ```tug-eks k get pods```
* View logs ```tug-eks k logs -f apicontent-blue-64777d67fd-bqvfm``` 

## LocalTests using a Rig
* Find the application-localTest.yml in the module that contains the tests you want to run
* Uncomment the line "domovm.sit.customer.deleteExistingCustomer: false"
* Before routing to the local running apiContent, run the test (at least enough to create the customer)
* Route to local apiContent
* Rerun the test

## Build and run local unit tests
* ./gradlew content-app:test

## Run a single sit test from the command line
* ```./gradlew :brandkit-app:testNGIT --tests com.domo.api.brandkit.chartColorPalettes.service.mapper.ChartColorPaletteMapperIT.create_shouldSucceed_whenValidInputs```
* Be sure you specify the correct module and test task (content-app has 2 test groups)
* ```./gradlew :content-app:testNGIT2 --tests com.domo.api.content.sit.sumo.resource.SumoResourceIT.getSumoTableCard```
