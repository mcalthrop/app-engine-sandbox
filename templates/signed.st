{% extends "index.html" %}

{% block title %}Your comment{% endblock %}

{% block content %}

    <p>You wrote:</p>
    <pre>{{ comments }}</pre>

{% endblock %}