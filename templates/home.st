{% extends "index.html" %}

{% block title %}Write your comment here{% endblock %}

{% block content %}
    <p>this is the day<br>your life will surely change, {{ userNickname }}</p>

    <form action="/sign" method="post">
        <div><textarea name="content" rows="3" cols="60"></textarea></div>
        <div><input type="submit" value="Sign Guestbook"></div>
    </form>
{% endblock %}