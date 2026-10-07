from __future__ import annotations

SITE_NAME = 'Cessnock Motor Cycle Club'
SITE_DESCRIPTION = (
    'The oldest active motorcycle club in Australia, riding in the Hunter '
    'Valley since before 1923. Regular rides and catch-ups, a welcoming '
    'community, and home of the Australian Postie Bike GP.'
)
NAV_ITEMS = [
    {'label': 'Home', 'slug': ''},
    {'label': 'Our story', 'slug': 'about'},
    {'label': 'What\'s on', 'slug': 'events'},
    {'label': 'Gallery', 'slug': 'gallery'},
    {'label': 'Postie Bike GP', 'slug': 'postie-bike-gp'},
    {'label': 'Membership', 'slug': 'membership'},
    {'label': 'Contact', 'slug': 'contact'},
]

FOOTER_LINKS = [
    {'label': 'Club officials', 'href': 'officials', 'external': False},
    {'label': 'Meetings', 'href': 'meetings', 'external': False},
    {'label': 'Remembrance', 'href': 'remembrance', 'external': False},
    {'label': 'Gallery', 'href': 'gallery', 'external': False},
    {'label': 'Sponsors', 'href': 'sponsors', 'external': False},
    {'label': 'Archive', 'href': 'archive', 'external': False},
    {'label': 'Facebook', 'href': 'https://www.facebook.com/cessnockmotorcycleclub/', 'external': True},
    {'label': 'YouTube', 'href': 'https://www.youtube.com/user/cessnockmcc/', 'external': True},
    {'label': 'Email us', 'href': 'mailto:info@cessnockmcc.com.au', 'external': True},
]

PAGES = [
    {
        'slug': '',
        'title': 'A century of motorcycling, and still riding',
        'eyebrow': 'Incorporated 1923 · Cessnock NSW',
        'intro': 'Cessnock Motor Cycle Club is the oldest active motorcycle club in Australia. The racing years made our name — the riding, and the people, keep us going.',
        'description': SITE_DESCRIPTION,
        'body_class': 'hero-home',
        'hero_image': 'assets/legacy-sweep/gallery-03.jpg',
        'content': '''
<section class="card">
  <h2>More than a century, in six moments</h2>
  <ul class="timeline">
    <li><span class="year">Before 1923</span><p>Riders are already gathering around Cessnock.</p></li>
    <li><span class="year">1923</span><p>The club is formally incorporated.</p></li>
    <li><span class="year">1978</span><p>The Australian Four Day Enduro is born here.</p></li>
    <li><span class="year">2014</span><p>The first Australian Postie Bike GP closes the CBD.</p></li>
    <li><span class="year">2023</span><p>Centenary — 100 years since incorporation.</p></li>
    <li><span class="year">Today</span><p>Australia's oldest active motorcycle club, now a social one.</p></li>
  </ul>
  <p><a class="button button-secondary" href="about/">Read the full story</a></p>
</section>
<section class="grid two-up">
  <article class="card prose">
    <h2>The club today</h2>
    <p>It's been years since our last competitive event, and that suits us fine. The calendar now is social rides through the Hunter, club catch-ups at the Khartoum Hotel, and the volunteer effort behind the <a href="postie-bike-gp/">Australian Postie Bike GP</a>.</p>
    <p>New faces are always welcome — you don't need to be fast, and you don't even need a dirt bike.</p>
  </article>
  <aside class="card card-accent card-v">
    <h2>Be part of it</h2>
    <ul class="link-list">
      <li><a href="events/">See what's on</a></li>
      <li><a href="membership/">Join the club — $30 a year</a></li>
      <li><a href="meetings/">Come to a meeting</a></li>
      <li><a href="get-involved/">Volunteer at the GP</a></li>
    </ul>
    <p class="btn-fill"><a class="button" href="membership/">Become a member</a></p>
  </aside>
</section>
<section class="gallery-grid">
  <img class="gallery-image" src="/assets/legacy-sweep/gallery-01.jpg" alt="From the club photo archive">
  <img class="gallery-image" src="/assets/legacy-sweep/gallery-05.jpg" alt="From the club photo archive">
  <img class="gallery-image" src="/assets/legacy-sweep/gallery-07.jpg" alt="From the club photo archive">
</section>
<section class="card gp-banner">
  <img class="media-image" src="/assets/media/postie-gp-hero.jpg" alt="Australian Postie Bike GP racing through the Cessnock CBD">
  <div>
    <p class="meta-line">Our signature event</p>
    <h2>Australian Postie Bike GP</h2>
    <p>Team racing on Honda CT110s through closed streets in the Cessnock CBD — hosted and run by the club since 2014.</p>
    <p><a class="button" href="postie-bike-gp/">About the GP</a></p>
  </div>
</section>
'''.strip(),
    },
    {
        'slug': 'about',
        'title': 'Our story',
        'eyebrow': 'Incorporated 1923',
        'intro': 'The oldest active motorcycle club in Australia — more than a century of riding in Cessnock, and a new chapter built around social riding.',
        'description': 'The history and present-day focus of Cessnock Motor Cycle Club — the oldest active motorcycle club in Australia, incorporated 1923.',
        'hero_image': 'assets/legacy-sweep/gallery-03.jpg',
        'content': '''
<section class="card prose">
  <p>Cessnock Motor Cycle Club is the <strong>oldest active motorcycle club in Australia</strong>. It was formally incorporated in <strong>1923</strong> — and riders were already gathering here for some years before that, though how many is no longer known. Generations of local families have ridden, raced, volunteered, and made lifelong friends through the club — from grass track and enduro through to the club days and social rides of today.</p>
  <p>Cessnock earned a reputation as one of Australia's great dirt bike towns. The Australian Four Day Enduro began here, and in 1992 the club community was at the heart of bringing the International Six Days Enduro to Cessnock — the biggest event the town had seen.</p>
</section>
<section class="card">
  <h2>More than a century, in short</h2>
  <ul class="timeline">
    <li><span class="year">Before 1923</span><p>Riders were already gathering around Cessnock. The club's origins predate its paperwork by an unknown number of years.</p></li>
    <li><span class="year">1923</span><p>The club is formally incorporated in Cessnock. This is the date the club counts from.</p></li>
    <li><span class="year">1978</span><p>The Australian Four Day Enduro is born in Cessnock, the event's original home.</p></li>
    <li><span class="year">1992</span><p>The International Six Days Enduro comes to Cessnock, powered by club volunteers.</p></li>
    <li><span class="year">2013</span><p>The club celebrates its 90th anniversary.</p></li>
    <li><span class="year">2014</span><p>The first Australian Postie Bike GP takes over the streets of the Cessnock CBD.</p></li>
    <li><span class="year">2018</span><p>The club runs the Australian Four Day Enduro — its most recent competitive event. <a href="../archive/a4de-2018/">See the archive page</a>.</p></li>
    <li><span class="year">2023</span><p>The club celebrates its centenary — 100 years since formal incorporation.</p></li>
    <li><span class="year">Today</span><p>The oldest active motorcycle club in Australia, and a social one: regular rides, club catch-ups, and one very big day of postie bike racing each year.</p></li>
  </ul>
</section>
<section class="card prose">
  <h2>The club today</h2>
  <p>It has been some years since the club last ran competitive events, and that's a deliberate change of pace. The focus now is <strong>social riding and club life</strong> — organised rides, regular get-togethers, and keeping the club's history and community alive for the next generation.</p>
  <p>The club still hosts the <a href="../postie-bike-gp/">Australian Postie Bike GP</a>, our signature public event, and remains a proud part of the Cessnock community.</p>
</section>
<section class="grid thirds">
  <article class="card card-v">
    <h2>Club officials</h2>
    <p>Meet the committee who keep the club running.</p>
    <p class="btn-fill"><a class="button button-secondary" href="../officials/">View officials</a></p>
  </article>
  <article class="card card-v">
    <h2>Club constitution</h2>
    <p>A plain-language summary of the club constitution, with the full PDF to download.</p>
    <p class="btn-fill"><a class="button button-secondary" href="../constitution/">Read summary</a></p>
  </article>
  <article class="card card-v">
    <h2>Remembrance</h2>
    <p>A tribute to John Hall and his impact on the club and the wider riding community.</p>
    <p class="btn-fill"><a class="button button-secondary" href="../remembrance/">Read tribute</a></p>
  </article>
</section>
'''.strip(),
    },
    {
        'slug': 'officials',
        'title': 'Club officials',
        'eyebrow': 'Executive committee',
        'intro': 'Committee roles published on the club\'s existing public website.',
        'description': 'Executive committee listing for Cessnock Motor Cycle Club.',
        'content': '''
<section class="card">
  <div class="split-list">
    <div>
      <h2>Office bearers</h2>
      <ul class="detail-list">
        <li><strong>President:</strong> David Blake</li>
        <li><strong>Vice President:</strong> Jason Chapman</li>
        <li><strong>Race Secretary:</strong> Matthew Vogt</li>
        <li><strong>Treasurer:</strong> Glen Toner</li>
        <li><strong>Equipment Steward:</strong> Dave Cocking</li>
        <li><strong>Public Officer:</strong> David Blake</li>
        <li><strong>Publicity Officer:</strong> Steven Parish</li>
      </ul>
    </div>
    <div>
      <h2>Need the latest contacts?</h2>
      <p>Committee roles can change over time. If you are making an enquiry about events, volunteering, sponsorship, or membership, the safest contact point is the club email.</p>
      <p><a class="button" href="mailto:info@cessnockmcc.com.au">Email the club</a></p>
    </div>
  </div>
</section>
'''.strip(),
    },
    {
        'slug': 'constitution',
        'title': 'Club constitution summary',
        'eyebrow': 'Governance and membership',
        'intro': 'A concise summary of the constitution text published on the legacy website.',
        'description': 'Summary of the constitution content published for Cessnock Motor Cycle Club.',
        'content': '''
<section class="card prose">
  <p>The current website publishes a full incorporated association constitution covering membership, committee responsibilities, meetings, voting, disputes, insurance, funds, and record keeping. Rather than reproducing a long block of legacy legal text here, this version keeps the core points easy to scan.</p>
  <p><a class="button" href="../assets/docs/club-constitution.pdf">Download constitution PDF</a></p>
  <h2>Highlights from the published constitution</h2>
  <ul>
    <li>Membership is approved by the committee after nomination and payment of applicable fees.</li>
    <li>Members may resign, be suspended, or be expelled under the rules set out in the constitution.</li>
    <li>The committee manages the affairs of the association and includes the president, vice-president, treasurer, secretary, and ordinary committee members.</li>
    <li>Annual general meetings and special general meetings are governed by notice, quorum, voting, and adjournment requirements.</li>
    <li>The constitution also covers disputes, insurance, the management of funds, the custody of books, and the service of notices.</li>
  </ul>
  <p>If you need the official current version of the constitution for governance or compliance purposes, please request it directly from the club committee.</p>
  <p><a class="button" href="mailto:info@cessnockmcc.com.au?subject=Constitution%20request">Request the constitution</a></p>
</section>
'''.strip(),
    },
    {
        'slug': 'gallery',
        'title': 'Gallery',
        'eyebrow': 'Photo archive',
        'intro': 'A preserved set of public club images copied from the legacy site photo gallery and related public pages.',
        'description': 'Historic public photo gallery preserved from the legacy Cessnock Motor Cycle Club website.',
        'content': '''
<section class="card prose">
  <p>This gallery preserves the public photo images exposed on the legacy site during the migration. It gives the new static build a place to retain that visual history even without the original dynamic gallery system.</p>
</section>
<section class="gallery-grid">
  <img class="gallery-image" src="/assets/legacy-sweep/gallery-01.jpg" alt="Historic club gallery image 1">
  <img class="gallery-image" src="/assets/legacy-sweep/gallery-02.jpg" alt="Historic club gallery image 2">
  <img class="gallery-image" src="/assets/legacy-sweep/gallery-03.jpg" alt="Historic club gallery image 3">
  <img class="gallery-image" src="/assets/legacy-sweep/gallery-04.jpg" alt="Historic club gallery image 4">
  <img class="gallery-image" src="/assets/legacy-sweep/gallery-05.jpg" alt="Historic club gallery image 5">
  <img class="gallery-image" src="/assets/legacy-sweep/gallery-06.jpg" alt="Historic club gallery image 6">
  <img class="gallery-image" src="/assets/legacy-sweep/gallery-07.jpg" alt="Historic club gallery image 7">
  <img class="gallery-image" src="/assets/legacy-sweep/gallery-08.jpg" alt="Historic club gallery image 8">
</section>
<section class="card prose">
  <h2>Other preserved files</h2>
  <ul>
    <li><a href="../assets/docs/club-constitution.pdf">Club constitution PDF</a></li>
    <li><a href="../assets/legacy-sweep/postie-gp-2015.jpg">Postie GP 2015 image</a></li>
    <li><a href="../assets/legacy-sweep/aus-gp-postie-tile.jpg">Aus GP Postie tile image</a></li>
  </ul>
</section>
'''.strip(),
    },
    {
        'slug': 'meetings',
        'title': 'Club meetings',
        'eyebrow': 'Monthly catch-up',
        'intro': 'The club welcomes members and interested locals to attend and help shape the season ahead.',
        'description': 'Meeting time and location for Cessnock Motor Cycle Club.',
        'content': '''
<section class="card prose">
  <p>Cessnock Motor Cycle Club holds general meetings at <strong>7:00pm on the first Tuesday of every month</strong> at the <strong>Khartoum Hotel, Kitchener</strong>, with two exceptions: there is <strong>no meeting in January</strong>, and in <strong>November</strong> the meeting moves to the <strong>second Tuesday</strong> (the first Tuesday is Melbourne Cup day).</p>
  <p>Anyone interested in the club is welcome to attend, contribute ideas, and help shape what the club does next — you don't need to be a member.</p>
  <p>Memberships are available online, and meetings are the easiest way to find out about rides, volunteering, and club life.</p>
  <p><a class="button" href="../membership/">View membership information</a></p>
</section>
'''.strip(),
    },
    {
        'slug': 'remembrance',
        'title': 'Remembrance',
        'eyebrow': 'In memory of John Hall',
        'intro': 'A tribute carried over from the legacy site, reflecting on John Hall\'s leadership, generosity, and influence.',
        'description': 'Memorial tribute to John Hall from the Cessnock Motor Cycle Club community.',
        'content': '''
<section class="card prose">
  <p>The original club website includes a moving tribute written by life member Glenn "Crasha" Toner about John Hall. Rather than listing dates and achievements alone, the piece speaks about how John carried himself: calm under pressure, deeply knowledgeable, generous with his time, and respected by everyone around him.</p>
  <p>It remembers the energy around the 1992 International Six Days Enduro campaign in Cessnock, the Monday night planning meetings at the fire station, and the way John brought clarity and confidence whenever questions arose. The tribute also captures the personal side of his legacy: the race stories, the practical advice, and the sense that he was always willing to help riders and events be better.</p>
  <p>For those who knew him, the page remains a reminder of a rider, organiser, mentor, and friend whose influence went well beyond one event or one club role.</p>
</section>
'''.strip(),
    },
    {
        'slug': 'get-involved',
        'title': 'Get involved',
        'eyebrow': 'The club runs on volunteers',
        'intro': 'You don’t need to race — or even ride — to be part of the club.',
        'description': 'Ways to join in, volunteer, and support Cessnock Motor Cycle Club.',
        'content': '''
<section class="grid two-up">
  <article class="card prose">
    <h2>A club is its people</h2>
    <p>Everything the club does — the rides, the catch-ups, the Postie Bike GP — happens because members put their hands up. There are no paid staff; there never have been in more than a century.</p>
    <p>Whether you ride every weekend or haven't swung a leg over a bike in years, there's a place for you. Plenty of our members are here for the company as much as the riding.</p>
  </article>
  <article class="card">
    <h2>Ways to help</h2>
    <ul class="detail-list">
      <li><strong>Come to a meeting</strong> — first Tuesday of the month, 7pm at the Khartoum Hotel, Kitchener. You don't need to be a member.</li>
      <li><strong>Help run the Postie Bike GP</strong> — marshals, setup crew, catering, and a dozen other jobs on the club's biggest day.</li>
      <li><strong>Lead or plan a social ride</strong> — know a good loop? Put it on the calendar.</li>
      <li><strong>Help with the history project</strong> — a century of photos, trophies, and stories worth preserving.</li>
    </ul>
  </article>
</section>
<section class="card prose">
  <h2>Ready when you are</h2>
  <p>Drop the club a line and we'll point you at something useful — or just come along to the next meeting or ride and say g'day.</p>
  <p><a class="button" href="mailto:info@cessnockmcc.com.au?subject=I%20want%20to%20help">Volunteer with the club</a></p>
</section>
'''.strip(),
    },
    {
        'slug': 'membership',
        'title': 'Membership',
        'eyebrow': 'Join the club',
        'intro': 'Cheap as chips, and you become part of more than a century of history.',
        'description': 'Membership information and pricing for Cessnock Motor Cycle Club.',
        'content': '''
<section class="grid two-up">
  <article class="card prose">
    <h2>What membership gives you</h2>
    <ul>
      <li>Be part of the oldest active motorcycle club in Australia, riding since before 1923.</li>
      <li>Join social rides, club days, and get-togethers through the year.</li>
      <li>Motorcycling NSW affiliation — licensing and event insurance are available through the club when needed.</li>
      <li>Help keep the Australian Postie Bike GP and the club's community work going.</li>
    </ul>
  </article>
  <article class="card card-accent">
    <h2>Prices</h2>
    <ul class="detail-list">
      <li><strong>Single membership:</strong> $30.00 per year</li>
      <li><strong>Family membership:</strong> $50.00 per year for up to 6 family members</li>
    </ul>
  </article>
</section>
<section class="card prose">
  <h2>How to join</h2>
  <p>Sign up through the Motorcycling NSW Ridernet system — choose <strong>Cessnock Motor Cycle Club</strong> from the club list. Or come along to a meeting and join on the night.</p>
  <p><a class="button" href="https://ridernet.com.au/member/index.cfm?p=register">Join via Ridernet</a></p>
</section>
'''.strip(),
    },
    {
        'slug': 'postie-bike-gp',
        'title': 'Australian Postie Bike GP',
        'eyebrow': 'Our signature public event',
        'intro': 'Once a year the club closes the streets of Cessnock for team racing on Honda CT110 postie bikes. It’s the biggest day on our calendar — and everyone’s invited.',
        'description': 'The Australian Postie Bike GP, hosted by Cessnock Motor Cycle Club in the Cessnock CBD.',
        'hero_image': 'postie-gp-hero.jpg',
        'content': '''
<section class="card prose">
  <p>The Australian Postie Bike GP is a family-friendly team race held on closed streets around the Cessnock CBD, with local cafes trading al fresco to the crowds lining the course. Teams of riders and pit crew race the iconic Honda CT110 — quick enough to be a spectacle, slow enough that spectators see every lap.</p>
  <p>The event is run entirely by club volunteers and has become one of the best-known postie bike races in the country. It's a big part of who we are — but it's one day a year. The rest of the club calendar is social rides and catch-ups.</p>
</section>
<section class="grid two-up">
  <article class="card media-card">
    <img class="media-image" src="/assets/legacy-sweep/postie-gp-2015.jpg" alt="Racing at a past Australian Postie Bike GP">
  </article>
  <article class="card media-card">
    <img class="media-image" src="/assets/media/postie-gp-course-layout.png" alt="Postie Bike GP street circuit layout through central Cessnock">
  </article>
</section>
<section class="grid two-up">
  <article class="card card-v">
    <h2>Past events</h2>
    <p>Results, photos, and course details from previous years are kept in the club archive.</p>
    <p class="btn-fill"><a class="button button-secondary" href="../archive/postie-bike-gp-2019/">Postie Bike GP 2019</a></p>
  </article>
  <article class="card card-v card-accent">
    <h2>Help run the next one</h2>
    <p>It takes dozens of volunteers to close the streets and run the day. Marshals, setup, catering — every job matters.</p>
    <p class="btn-fill"><a class="button" href="../get-involved/">Get involved</a></p>
  </article>
</section>
'''.strip(),
    },
    {
        'slug': 'sponsors',
        'title': 'Sponsors',
        'eyebrow': 'Support the businesses that support the club',
        'intro': 'Community events are made possible by sponsors who back local riding and local volunteers.',
        'description': 'Sponsor acknowledgement page for Cessnock Motor Cycle Club.',
        'content': '''
<section class="card prose">
  <p>Cessnock Motor Cycle Club thanks all of the sponsors who have supported the club over the years. The original site encourages members and visitors to support those businesses in return and recognise the role they play in keeping grassroots motorcycle sport strong in the region.</p>
  <h2>Featured sponsor from the legacy site</h2>
  <div class="media-inline">
    <img class="media-logo" src="/assets/media/sponsor-greenslipcalculator.jpg" alt="GreenSlipCalculator.com.au logo">
    <p><strong>GreenSlipCalculator.com.au</strong> was highlighted as a club sponsor, helping Australians compare greenslip prices, products, services, and insurers online.</p>
  </div>
  <p><a class="button button-secondary" href="http://greenslipcalculator.com.au/">Visit sponsor website</a></p>
</section>
<section class="card media-card">
  <img class="media-image" src="/assets/media/sponsor-khartoum-hotel.jpeg" alt="Khartoum Hotel sponsor image from the legacy site">
</section>
<section class="card prose">
  <h2>Interested in sponsoring the club?</h2>
  <p>If you would like to support the club, its events, or junior and community participation in off road motorcycling, get in touch with the committee.</p>
  <p><a class="button" href="mailto:info@cessnockmcc.com.au?subject=Sponsorship%20enquiry">Sponsorship enquiry</a></p>
</section>
'''.strip(),
    },
    {
        'slug': 'archive',
        'title': 'Archive',
        'eyebrow': 'Public highlights from the legacy site',
        'intro': 'A simplified archive for notable public events and historical content worth keeping.',
        'description': 'Archive of notable public content from the legacy Cessnock Motor Cycle Club website.',
        'content': '''
<section class="grid two-up">
  <article class="card media-card card-v">
    <img class="media-image" src="/assets/media/gallery-general.jpg" alt="General club gallery image">
    <h2>Australian Four Day Enduro 2018</h2>
    <p>The legacy event listing notes the 40th anniversary edition of the Australian 4 Day Enduro, returning to Cessnock where it all started.</p>
    <p class="btn-fill"><a class="button button-secondary" href="a4de-2018/">Open archive page</a></p>
  </article>
  <article class="card media-card card-v">
    <img class="media-image" src="/assets/media/postie-gp-hero.jpg" alt="Australian Postie Bike GP 2019 event image">
    <h2>Australian Postie Bike GP 2019</h2>
    <p>A family-friendly street event in the Cessnock CBD featuring team racing on Honda CT110 Postie Bikes.</p>
    <p class="btn-fill"><a class="button button-secondary" href="postie-bike-gp-2019/">Open archive page</a></p>
  </article>
</section>
<section class="card prose">
  <h2>Looking for current event updates?</h2>
  <p>The old website used dynamic news and events modules. For a simplified static setup, it makes more sense to keep major historical items here and use social channels or a future editable content workflow for up-to-date event announcements.</p>
  <p><a class="button" href="https://www.facebook.com/cessnockmotorcycleclub/">Follow updates on Facebook</a></p>
</section>
'''.strip(),
    },
    {
        'slug': 'archive/a4de-2018',
        'title': 'Australian Four Day Enduro 2018',
        'eyebrow': 'Archive item',
        'intro': 'A preserved summary of the public event listing from the legacy site.',
        'description': 'Archive summary for the 2018 Australian Four Day Enduro listing.',
        'content': '''
<section class="card prose">
  <p>The legacy site records this event as the <strong>40th anniversary edition of the Australian 4 Day Enduro</strong>, returning to Cessnock where the event began.</p>
  <img class="media-image" src="/assets/media/gallery-general.jpg" alt="General club image used as an archive illustration">
  <ul>
    <li><strong>Dates:</strong> 3 April 2018 to 7 April 2018</li>
    <li><strong>Location:</strong> Cessnock Showground</li>
  </ul>
  <p>This page is kept as a historical reference within the simplified static rebuild.</p>
  <p><a class="button button-secondary" href="../">Back to archive</a></p>
</section>
'''.strip(),
    },
    {
        'slug': 'archive/postie-bike-gp-2019',
        'title': 'Australian Postie Bike GP 2019',
        'eyebrow': 'Archive item',
        'intro': 'A preserved summary of one of the club\'s standout public event pages.',
        'description': 'Archive summary for the 2019 Australian Postie Bike GP.',
        'content': '''
<section class="card prose">
  <img class="media-image" src="/assets/media/postie-gp-hero.jpg" alt="Australian Postie Bike GP 2019 banner image">
  <p>The Australian Postie Bike GP was presented as a family-friendly team race held on closed streets around the Cessnock CBD. By 2019 the event was in its sixth year and had built a strong profile with local riders, first-timers, and well-known names from the motorcycle community.</p>
  <div class="media-inline">
    <img class="media-logo" src="/assets/media/postie-gp-mitsubishi-logo.png" alt="Cessnock Mitsubishi sponsor logo">
    <p>The original page prominently thanked Cessnock Mitsubishi as the major sponsor for the 2019 event, alongside the public race information and course details.</p>
  </div>
  <h2>Key details from the legacy page</h2>
  <ul>
    <li><strong>Sign on and scrutineering:</strong> Saturday 9 November 2019</li>
    <li><strong>Race day:</strong> Sunday 10 November 2019</li>
    <li><strong>Format:</strong> Two-rider teams on Honda CT110 Postie Bikes with pit crew support</li>
    <li><strong>Course:</strong> A street circuit through central Cessnock and the TAFE precinct</li>
  </ul>
  <img class="media-image" src="/assets/media/postie-gp-course-layout.png" alt="Australian Postie Bike GP course layout">
  <p>The original page also outlined qualifying, the Cessnock Cup, a women's race, the main endurance-format GP, and recognition for major sponsor Cessnock Mitsubishi.</p>
  <p><a class="button button-secondary" href="../">Back to archive</a></p>
</section>
'''.strip(),
    },
    {
        'slug': 'contact',
        'title': 'Contact the club',
        'eyebrow': 'Get in touch',
        'intro': 'For membership, events, sponsorship, or general enquiries, start with the club email.',
        'description': 'Contact details for Cessnock Motor Cycle Club.',
        'content': '''
<section class="grid two-up">
  <article class="card prose">
    <h2>Postal address</h2>
    <p>
      Cessnock Motorcycle Club<br>
      PO Box 287<br>
      Cessnock NSW 2325
    </p>
  </article>
  <article class="card prose">
    <h2>Email</h2>
    <p><a href="mailto:info@cessnockmcc.com.au">info@cessnockmcc.com.au</a></p>
    <p>The club is volunteer-run, so responses may not be instant. Thanks in advance for your patience.</p>
  </article>
</section>
<section class="card prose">
  <h2>Social channels</h2>
  <p>For general updates and public-facing club activity, you can also follow the club on Facebook or YouTube.</p>
  <ul class="detail-list">
    <li><a href="https://www.facebook.com/cessnockmotorcycleclub/">Facebook</a></li>
    <li><a href="https://www.youtube.com/user/cessnockmcc/">YouTube</a></li>
  </ul>
</section>
'''.strip(),
    },
]
