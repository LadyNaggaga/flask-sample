# Aspire Dashboard ♥️ Flask
To run the Aspire Dashboard first run:

```cli
docker run --rm -it -p 18888:18888 -p 4317:18889 -d --name aspire-dashboard \
    mcr.microsoft.com/dotnet/nightly/aspire-dashboard:8.0-preview
```

Locate the dashboard url and api key with the following Docker command:

```cli
docker logs aspire-dashboard
```

To run this application:

```cli
flask --debug run
```
