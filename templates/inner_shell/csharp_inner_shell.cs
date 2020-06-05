{{ rendered_imports }}


{% for dkey in rendered_dkeys %}
{{ dkey }}
{% endfor %}

{{ rendered_decrypter }}

{{ rendered_executor }}

{% for rpm in rendered_pre_modules %}
{{ rpm }}
{% endfor %}

{% for rpm in rendered_post_modules %}
{{ rpm }}
{% endfor %}

{{ rendered_payload_main }}
