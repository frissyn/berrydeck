{% extends "_layouts/default.vue" %}{% block title %}Editing '{{ s['semantic-fn'] }}' - BerryDeck{% endblock %}{% block navend %}
<div class="flex-none"><a class="btn btn-ghost gap-2" href="/editor/download"><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" aria-hidden="true" class="w-6 h-6"><path stroke-linecap="round" stroke-linejoin="round" d="M12 9.75v6.75m0 0l-3-3m3 3l3-3m-8.25 6a4.5 4.5 0 01-1.41-8.775 5.25 5.25 0 0110.233-2.33 3 3 0 013.758 3.848A3.752 3.752 0 0118 19.5H6.75z"></path></svg>Download Savefile</a></div>{% endblock %}

{% block content%}
<div id="mount" class="min-h-[88vh] p-4 sm:p-6 md:p-8">
  <h1 class="hero-title mb-4">Editing '<b>{{ s['semantic-fn'] }}</b>'</h1>

<!--- BEGIN BLOCK ~ sabefile tab buttons --->
<div id="blockA" class="tabs"><button class="tab tab-bordered tab-active" onclick="tabover(event, 'meta', 'blockA')">Metadata</button><button class="tab tab-bordered" onclick="tabover(event, 'stats', 'blockA')">Statistics</button><button class="tab tab-bordered" onclick="tabover(event, 'mods', 'blockA')">Modifiers</button><button class="tab tab-bordered" onclick="tabover(event, 'flags', 'blockA')">Story Flags</button></div>
<!--- BEGIN END --->

<!--- BEGIN BLOCK ~ savefile tabs --->
 <div for="blockA"><div id="meta" class="tab-content bg-base-200 mb-2 p-4"><form name="meta" onsubmit="commit(event, this)"> <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-4"> <div class="col-auto"> <div class="form-control w-full"> <label class="label"><span class="label-text"><b>Savefile Name</b></span></label> <input name="name" type="text" value="{{save.name}}" class="input input-bordered w-full"/> </div></div><div class="col-auto"> <div class="form-control w-full"> <label class="label"><span class="label-text"><b>Game Version</b></span><span class="label-text-alt">Locked</span></label> <input name="version" type="text" value="{{save.version}}" class="input input-bordered w-full" readonly/> </div></div><div class="col-auto">{% set clock=save.time.value.iclock() %}<div class="form-control w-full"> <label class="label"> <span class="label-text"><b>Playtime</b></span><span class="label-text-alt"><b>Format:</b> HH:MM:SS.ms</span> </label> </div><div class="bg-base-100 rounded border border-base-content border-opacity-20 p-3"> <input name="hours" type="number" value="{{clock[0]}}" placeholder="Hours" min="0" class="input-number w-16 my-0"> <span class="mx-2"><b>:</b></span> <input name="mins" type="number" value="{{clock[1]}}" placeholder="Minutes" min="0" max="59" class="input-number w-16 my-0"> <span class="mx-2"><b>:</b></span> <input name="secs" type="number" value="{{clock[2]}}" placeholder="Seconds" min="0" max="59" class="input-number w-16 my-0"> <span class="mx-2"><b>.</b></span> <input name="ms" type="number" value="{{clock[3]}}" placeholder="Milliseconds" min="0" max="999" class="input-number w-16 my-0"> </div></div><div class="col-auto"> <div class="form-control w-full"> <label class="label"><span class="label-text"><b>Last Save (Epoch)</b></span><span class="label-text-alt">Locked</span></label> <input name="lastsave" type="text" value="{{save.lastsave}}" class="input input-bordered w-full" readonly/> </div></div><div class="col-auto"> <div class="form-control w-full"> <label class="label"><span class="label-text"><b>XML Namespace</b></span><span class="label-text-alt">Locked</span></label> <input name="xmlns" type="text" value="http://www.w3.org/2001/XMLSchema" class="input input-bordered w-full" readonly/> </div></div></div><br><div class="form-control rounded w-full"> <div class="object-right ml-auto mr-0"> <input type="reset" class="btn btn-sm rounded-l"/> <input type="submit" value="Commit Changes" class="btn btn-sm btn-accent rounded-r"/> </div></div></form> </div><div id="stats" class="tab-content bg-base-200 mb-2 p-4 hidden"> <form name="stats" onsubmit="commit(event, this)"> <div class="grid grid-cols-1 sm:grid-cols-5 gap-4"> <div class="cols-auto sm:col-span-5"> <h1 class="hero-title mb-2"><b>Completed Actions:</b></h1> <div class="stats shadow w-full">{% for name in lexicon.SEMANTICS['stats'] %}<div class="stat"> <div class="stat-value text-xl sm:text-2xl md:text-3xl"> <input name="{{name}}" type="number" min="0" value="{{save.get(name)}}" class="input-ghost bg-inherit m-0 p-0 w-full"> </div><div class="stat-desc">{{name | title}}</div></div>{% endfor %}</div></div><div class="cols-auto"> <h1 class="hero-title mb-2"><b>Miscellaneous:</b></h1> <div class="stats shadow w-full"> <div class="stat"> <div class="stat-value text-xl sm:text-2xl md:text-3xl"> <input name="UnlockedAreas" type="number" min="1" max="10" value="{{save.unlockedareas}}" class="input-ghost bg-inherit m-0 p-0 w-full"/> </div><div class="stat-desc">Unlocked Chapters</div></div></div></div><div class="cols-auto sm:col-span-2"> <h1 class="hero-title mb-2"><b>Collected Strawberries:</b></h1> <div class="stats shadow w-full"><div class="stat"> <div class="stat-value text-xl sm:text-2xl md:text-3xl"> <input name="TotalStrawberries" type="number" min="0" max="202" value="{{ save.totalstrawberries }}" class="input-ghost bg-inherit m-0 p-0 w-full"> </div><div class="stat-desc">Total Strawberries</div></div><div class="stat"> <div class="stat-value text-xl md:text-3xl"> <input name="TotalGoldenStrawberries" type="number" min="0" max="26" value="{{ save.totalgoldenstrawberries }}" class="input-ghost bg-inherit m-0 p-0 w-full"> </div><div class="stat-desc">Golden Strawberries</div></div></div></div></div><br><div class="form-control rounded w-full"> <div class="object-right ml-auto mr-0"> <input type="reset" class="btn btn-sm rounded-l"/> <input type="submit" value="Commit Changes" class="btn btn-sm btn-accent rounded-r"/> </div></div></form> </div><div id="mods" class="tab-content bg-base-200 mb-2 p-4 hidden"> <form name="mods" onsubmit="commit(event, this)"> <div class="grid grid-cols-1 md:grid-cols-4 gap-4"> <div class="cols-auto md:col-span-1"> <h1 class="hero-title"><b>Game Modes:</b></h1>{% for name in lexicon.SEMANTICS["modes"] %}<label class="label cursor-pointer w-full"> <span class="label-text">{{ name | title }}&nbsp;&nbsp;&nbsp;</span> <input name="{{name}}" type="checkbox" class="toggle toggle-secondary" onclick="toggleUse('{{name}}')"{{ save.get(name) | check}} /> </label>{% endfor %}</div><div class="cols-auto md:col-span-3"> <h1 class="hero-title"><b>Variants:</b></h1> <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 md:gap-x-4">{% for name in lexicon.SEMANTICS["variants"] %}<div class="cols-auto"><label class="label w-full sm:max-md:w-52 {% if save.variantmode %}cursor-pointer{% else %}cursor-not-allowed{% endif %}"><span class="label-text {% if not save.variantmode %}text-opacity-20{% endif %}">{{ name | title }}&nbsp;&nbsp;&nbsp;</span> <input name="{{name}}" type="checkbox" class="toggle toggle-secondary VariantMode" {{ save.get(name) | check }} {% if not save.variantmode %}disabled{% endif %}/> </label> </div>{% endfor %}</div></div><div class="cols-auto md:col-span-4"> <h1 class="hero-title"><b>Assists:</b></h1> <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 md:gap-x-8">{% for name in lexicon.SEMANTICS['assists']['toggle'] %}<div class="cols-auto"> <label class="label w-full sm:max-md:w-52 {% if save.assistmode %}cursor-pointer{% else %}cursor-not-allowed{% endif %}"> <span class="label-text {% if not save.assistmode %}text-opacity-20{% endif %}">{{ name | title }}&nbsp;&nbsp;&nbsp;</span> <input name="{{name}}" type="checkbox" class="toggle toggle-secondary AssistMode" {{ save.get(name) | check }} {% if not save.assistmode %}disabled{% endif %}/> </label> </div>{% endfor %}<div class="cols-auto"> <label class="label w-full sm:max-md:w-52"> <span class="label-text {% if not access %}text-opacity-20{% endif %}">Dash Mode:&nbsp;</span> <select name="DashMode" class="select select-bordered md:w-48 AssistMode" {% if not save.assistmode %}disabled{% endif %}>{% for opt in save.assists.dashmode.options %}<option {% if opt == save.assists.dashmode.value %}selected{% endif %}>{{opt}}</option>{% endfor %}</select> </label> </div><div class="cols-auto"> <label class="label w-full sm:max-md:w-52"> <span class="label-text {% if not save.assistmode %}text-opacity-20{% endif %}">Game Speed:&nbsp;</span> <input name="GameSpeed" type="number" min="10" max="160" step="10" value="{{save.assists.gamespeed}}" class="input input-bordered md:w-48 AssistMode" {% if not save.assistmode %}disabled{% endif %}/> </label> </div></div></div></div><br><div class="form-control rounded w-full"> <div class="object-right ml-auto mr-0"> <input type="reset" class="btn btn-sm rounded-l"/> <input type="submit" value="Commit Changes" class="btn btn-sm btn-accent rounded-r"/> </div></div></form> </div><div id="flags" class="tab-content bg-base-200 mb-2 p-4 hidden"><form name="flags" onsubmit="commit(event, this)"><div class="grid grid-cols-1 md:grid-cols-3 gap-4"> <div class="col-auto"> <div class="form-control w-full"> <label class="label"><span class="label-text"><b>Theo's Sister's Name</b></span></label> <input name="TheoSisterName" type="text" value="{{ save.theosistername }}" class="input input-bordered w-full"/> </div></div><div class="cols-auto"> <div class="invisible sm:visible"><br></div><label class="label w-full sm:max-md:w-64"> <span class="label-text">Met Theo?&nbsp;&nbsp;&nbsp;</span> <input name="MetTheo" type="checkbox" class="checkbox checkbox-secondary" {% if ("MetTheo" in save.flags.value) %}checked{% endif %}/></label></div><div class="cols-auto"> <div class="invisible md:visible"><br></div><label class="label w-full sm:max-md:w-52"><span class="label-text">Theo Knows Your Name?&nbsp;&nbsp;&nbsp;</span> <input name="TheoKnowsName" type="checkbox" class="checkbox checkbox-secondary" {% if ("TheoKnowsName" in save.flags.value) %}checked{% endif %}/> </label> </div> <div class="cols-auto"><div class="invisible md:visible"><br></div><label class="label w-full sm:max-md:w-52"><span class="label-text">Revealed Farewell on the Map?&nbsp;&nbsp;&nbsp;</span> <input name="RevealedChapter9" type="checkbox" class="checkbox checkbox-secondary" {% if save.revealedchapter9.value %}checked{% endif %}/> </label> </div></div> <br><div class="form-control rounded w-full"><div class="object-right ml-auto mr-0"> <input type="reset" class="btn btn-sm rounded-l"/><input type="submit" value="Commit Changes" class="btn btn-sm btn-accent rounded-r"/></div></div></form></div></div>
<!--- END --->

<!--- BEGIN ~ savefile chapter tabs --->
<br><div id="blockB"><button class="tab tab-bordered tab-active" onclick="tabover(event, 'ch00', 'blockB')">Prologue</button><button class="tab tab-bordered" onclick="tabover(event, 'ch01', 'blockB')">Forsaken City</button><button class="tab tab-bordered" onclick="tabover(event, 'ch02', 'blockB')">Old Site</button><button class="tab tab-bordered" onclick="tabover(event, 'ch03', 'blockB')">Celestial Resort</button><button class="tab tab-bordered" onclick="tabover(event, 'ch04', 'blockB')">Golden Ridge</button><button class="tab tab-bordered" onclick="tabover(event, 'ch05', 'blockB')">Mirror Temple</button><button class="tab tab-bordered" onclick="tabover(event, 'ch06', 'blockB')">Reflection</button><button class="tab tab-bordered" onclick="tabover(event, 'ch07', 'blockB')">Summit</button><button class="tab tab-bordered" onclick="tabover(event, 'ch08', 'blockB')">Epilogue</button><button class="tab tab-bordered" onclick="tabover(event, 'ch09', 'blockB')">Core</button><button class="tab tab-bordered" onclick="tabover(event, 'ch10', 'blockB')">Farewell</button></div>
<!--- END --->

<!--- BEGIN ~ savefile chapter editor --->
<div for="blockB">
  {% for id, ch in lexicon.SEMANTICS["chapters"].items() %}{% set index = int(id) %}
  <div id="ch{{ id }}" class="tab-content bg-base-200 mb-2 p-4 {% if id != '00' %}hidden{% endif %}">
    {% for mode in ["A", "B", "C"] %}{% if ch[-1][mode] %}
    {% if mode != "A" %}<hr>{% endif %}
    <h1 class="hero-title my-2"><b>{{ mode }}-Side:</b></h1>
    <div class="grid grid-cols-1 sm:grid-cols-5 gap-4">
    <div class="col-span-2">
      <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 md:gap-x-4">
        {% for name, node in lexicon.ATTRIB %}{% if node["type"] == "boolean" %}
        <div class="cols-auto">
          <label class="label w-full sm:max-md:w-52">
            <span class="label-text">{{ name | title }}&nbsp;&nbsp;&nbsp;</span>
            <input name="{{ name }}" type="checkbox" 
              class="toggle toggle-secondary" {{ save.areas[index][mode].get(name) | check }}
            />
          </label>
        </div>
        {% endif %}{% endfor %}
      </div>
    </div>
    <div class="cols-auto sm:col-span-5 md:col-span-4">
    <div class="stats shadow w-full">
      {% for name in ["TotalStrawberries", "Deaths", "BestDeaths", "BestDashes"] %}
      <div class="stat">
        <div class="stat-value text-xl sm:text-2xl md:text-3xl">
        <input
          name="{{name}}" type="number" min="0" value="{{ save.areas[index][mode].get(name) }}" 
          class="input-ghost bg-inherit m-0 p-0 w-full"
        /> 
        </div>
        <div class="stat-desc">{{ name | title }}</div>
      </div>
      {% endfor %}
    </div>
    </div>
    </div>
    {% endif %}{% endfor %}
  <br><br>
  <div class="form-control rounded w-full"><div class="object-right ml-auto mr-0">
    <input type="reset" class="btn btn-sm rounded-l"/>
    <input type="submit" value="Commit Changes" class="btn btn-sm btn-accent rounded-r"/>
  </div></div>
  </div>
  {% endfor %}
</div>
<!--- END --->
</div>

<!--- BEGIN BLOCK ~ tailwind polyfills (for javascript manipulated elements) --->
<script src="static/scripts/commit.js"></script><script src="static/scripts/mods.js"></script><script src="static/scripts/tabs.js"></script><content class="alert alert-success alert-error text-opacity-20 shadow py-4 btn-sm btn-ghost loading hidden"></content>
<!--- END --->
{% endblock %}