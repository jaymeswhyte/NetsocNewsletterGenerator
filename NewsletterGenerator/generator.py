def generate(date, gifLink, eventDates, eventTitles, 
             eventImages, eventDescriptions, 
             gamingTitle, gamingLink, gamingImage, 
             gamingDescription, techTitle, techLink,
             techImage, techDescription):
    
    head = f'''
            <!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml"
    xmlns:o="urn:schemas-microsoft-com:office:office" lang="en">

<head>
    <title>Netsoc Newsletter {date}</title>
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <style type="text/css">
        a {{
            color: #56a4e8;
        }}

        #outlook a {{
            padding: 0;
        }}

        body {{
            margin: 0;
            padding: 0;
            -webkit-text-size-adjust: 100%;
            -ms-text-size-adjust: 100%;
        }}

        table,
        td {{
            border-collapse: collapse;
            mso-table-lspace: 0pt;
            mso-table-rspace: 0pt;
        }}

        img {{
            border: 0;
            height: auto;
            line-height: 100%;
            outline: none;
            text-decoration: none;
            -ms-interpolation-mode: bicubic;
        }}

        p {{
            display: block;
            margin: 13px 0;
        }}
    </style>
    <link href="https://fonts.googleapis.com/css2?family=Inknut+Antiqua:wght@400;500;600&amp;display=swap"
        rel="stylesheet" type="text/css" />
    <link href="https://fonts.googleapis.com/css2?family=Montserrat&amp;display=swap" rel="stylesheet"
        type="text/css" />
    <style type="text/css">
        @import url(https://fonts.googleapis.com/css2?family=Inknut+Antiqua:wght@400;500;600&amp;display=swap);
        @import url(https://fonts.googleapis.com/css2?family=Montserrat&amp;display=swap);
    </style>
    <style type="text/css">
        @media only screen and (min-width:480px) {{
            .mj-column-per-100 {{
                width: 100% !important;
                max-width: 100%;
            }}

            .mj-column-per-30 {{
                width: 30% !important;
                max-width: 30%;
            }}

            .mj-column-per-70 {{
                width: 70% !important;
                max-width: 70%;
            }}

            .mj-column-per-50 {{
                width: 50% !important;
                max-width: 50%;
            }}
        }}
    </style>
    <style type="text/css">
        @media only screen and (max-width:480px) {{
            table.mj-full-width-mobile {{
                width: 100% !important;
            }}

            td.mj-full-width-mobile {{
                width: auto !important;
            }}
        }}
    </style>
    <style type="text/css">
        a,
        span,
        td,
        th {{
            -webkit-font-smoothing: antialiased !important;
            -moz-osx-font-smoothing: grayscale !important;
        }}
    </style>
</head>

<body style="background-color:#171919;">
    <!--HEADER-->
    <div style="background-color:#171919;">
        <div style="margin:0px auto;max-width:600px;">
            <table role="presentation" style="width:100%;" cellspacing="0" cellpadding="0" border="0" align="center">
                <tbody>
                    <tr>
                        <td style="direction:ltr;font-size:0px;padding:20px 0;padding-bottom:0px;text-align:center;">
                            <div class="mj-column-per-100 mj-outlook-group-fix"
                                style="font-size:0px;text-align:left;direction:ltr;display:inline-block;vertical-align:middle;width:100%;">
                                <table role="presentation" style="vertical-align:middle;" width="100%" cellspacing="0"
                                    cellpadding="0" border="0">
                                    <tbody>
                                        <tr>
                                            <td style="font-size:0px;padding:10px 25px;word-break:break-word;"
                                                align="center">
                                                <table role="presentation"
                                                    style="border-collapse:collapse;border-spacing:0px;" cellspacing="0"
                                                    cellpadding="0" border="0">
                                                    <tbody>
                                                        <tr>
                                                            <td style="width:300px;">
                                                                <img alt="Logo"
                                                                    src="https://ci3.googleusercontent.com/meips/ADKq_NbYtb-vTfHKbanjyA69rmWfZLqb6NiU5eTLRwQsWpxXVI6c0yd41M7TmzKyzRTBiagQnKWnl7kqZnOGJC-_45jt5P944p5BHmRVpD43X8bVuW6ygWvZooa2SWpIAL7DFrgDkX2zBzXOFCr1BLAOf1SwxV_FMoiUDA=s0-d-e1-ft#https://media.discordapp.net/attachments/790410234790281216/1163275285953777664/1697416751248.png?"
                                                                    style="border:0;display:block;outline:none;text-decoration:none;height:auto;width:100%;font-size:14px;"
                                                                    width="150" height="auto" />
                                                            </td>
                                                        </tr>
                                                    </tbody>
                                                </table>
                                            </td>
                                        </tr>
                                    </tbody>
                                </table>
                            </div>
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>
        <div style="margin:0px auto;max-width:600px;">
            <table role="presentation" style="width:100%;" cellspacing="0" cellpadding="0" border="0" align="center">
                <tbody>
                    <tr>
                        <td style="direction:ltr;font-size:0px;padding:20px 0;text-align:center;">
                            <div class="mj-column-per-100 mj-outlook-group-fix"
                                style="font-size:0px;text-align:left;direction:ltr;display:inline-block;vertical-align:top;width:100%;">
                                <table role="presentation" style="vertical-align:top;" width="100%" cellspacing="0"
                                    cellpadding="0" border="0">
                                    <tbody>
                                        <tr>
                                            <td style="font-size:0px;padding:10px 25px;word-break:break-word;"
                                                align="center">
                                                <table role="presentation"
                                                    style="border-collapse:collapse;border-spacing:0px;" cellspacing="0"
                                                    cellpadding="0" border="0">
                                                    <tbody>
                                                        <tr>
                                                            <td style="width:550px;">
                                                                <img alt="image of the week"
                                                                    src="{gifLink}"
                                                                    style="border:0;display:block;outline:none;text-decoration:none;height:auto;width:100%;font-size:14px;"
                                                                    width="600" height="auto" />
                                                            </td>
                                                        </tr>
                                                    </tbody>
                                                </table>
                                            </td>
                                        </tr>
                                        <tr>
                                            <td style="font-size:0px;padding:10px 25px;word-break:break-word;"
                                                align="left">
                                                <div
                                                    style="font-family:Montserrat, Helvetica, Arial, sans-serif;font-size:18px;font-weight:400;line-height:24px;text-align:left;color:#dddddd;">
                                                    <h2
                                                        style="margin: 0; font-weight: 600; font-family: 'Inknut Antiqua', Helvetica, Arial, sans-serif; font-size: 24px; line-height: 30px;">
                                                        Here's what's coming up next week at Netsoc.</h2>
                                                </div>
                                            </td>
                                        </tr>
                                        
                                    </tbody>
                                </table>
                            </div>
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>
'''

    for i in range(0, len(eventDates)):
        head += f'''
        <!--EVENTS-->
        <div style="margin:0px auto;max-width:600px;">
            <table role="presentation" style="width:100%;" cellspacing="0" cellpadding="0" border="0" align="center">
                <tbody>
                    <tr>
                        <td style="direction:ltr;font-size:0px;padding:20px 0;text-align:center;">
                            <div class="mj-column-per-100 mj-outlook-group-fix"
                                style="font-size:0px;text-align:left;direction:ltr;display:inline-block;vertical-align:top;width:100%;">
                                <table role="presentation" style="vertical-align:top;" width="100%" cellspacing="0"
                                    cellpadding="0" border="0">
                                    <tbody>
                                        <tr>
                                            <td style="font-size:0px;padding:10px 25px;word-break:break-word;"
                                                align="left">
                                                <div
                                                    style="font-family:Montserrat, Helvetica, Arial, sans-serif;font-size:18px;font-weight:bold;line-height:24px;text-align:left;color:#dddddd;">
                                                    <h3style="margin: 0; font-size: 22px; line-height: 26px; font-weight: 600; font-family: 'Inknut Antiqua', Helvetica, Arial, sans-serif;">{eventDates[i]}</h3>
                                                </div>
                                            </td>
                                        </tr>
                                    </tbody>
                                </table>
                            </div>
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>
        <div style="margin:0px auto;max-width:600px;">
            <table role="presentation" style="width:100%;" cellspacing="0" cellpadding="0" border="0" align="center">
                <tbody>
                    <tr>
                        <td style="direction:ltr;font-size:0px;padding:0;text-align:center;">
                            <div class="mj-column-per-100 mj-outlook-group-fix"
                                style="font-size:0px;text-align:left;direction:ltr;display:inline-block;vertical-align:top;width:100%;">
                                <table role="presentation" style="vertical-align:top;" width="100%" cellspacing="0"
                                    cellpadding="0" border="0">
                                    <tbody>
                                        <tr>
                                            <td style="font-size:0px;padding:10px 25px;word-break:break-word;"
                                                align="left">
                                                <div
                                                    style="font-family:Montserrat, Helvetica, Arial, sans-serif;font-size:18px;font-weight:bold;line-height:24px;text-align:left;color:#dddddd;">
                                                    <h2
                                                        style="margin: 0; font-weight: 600; font-family: 'Inknut Antiqua', Helvetica, Arial, sans-serif; font-size: 24px; line-height: 30px;">
                                                        {eventTitles[i]}</h2>
                                                </div>
                                            </td>
                                        </tr>
                                        <tr>
                                            <td style="font-size:0px;padding:10px 25px;word-break:break-word;"
                                                align="left">
                                                <div
                                                    style="font-family:Montserrat, Helvetica, Arial, sans-serif;font-size:18px;font-weight:400;line-height:24px;text-align:left;color:#dddddd;">
                                                    <img width="600px" height="auto"
                                                        src="{eventImages[i]}"
                                                        alt="{eventTitles[i]} poster">
                                                    <p style="margin: 0;white-space: pre-line;">
                                                        {eventDescriptions[i]}
                                                    </p>
                                                </div>
                                            </td>
                                        </tr>
                                    </tbody>
                                </table>
                            </div>
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>
      <div style="margin:0px auto;max-width:600px;">
        <table role="presentation" style="width:100%;" cellspacing="0" cellpadding="0" border="0" align="center">
            <tbody>
                <tr>
                    <td style="direction:ltr;font-size:0px;padding:20px 0;text-align:center;">
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
    <div style="margin:0px auto;max-width:600px;">
        <table role="presentation" style="width:100%;" cellspacing="0" cellpadding="0" border="0" align="center">
            <tbody>
                <tr>
                    <td style="direction:ltr;font-size:0px;padding:0;text-align:center;">
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
'''
        
    head += f'''
<!--ARTICLES-->
        <div style="margin:0px auto;max-width:600px;">
            <table role="presentation" style="width:100%;" cellspacing="0" cellpadding="0" border="0" align="center">
                <tbody>
                    <tr>
                        <td style="direction:ltr;font-size:0px;padding:20px 0;text-align:center;">
                            <div class="mj-column-per-100 mj-outlook-group-fix"
                                style="font-size:0px;text-align:left;direction:ltr;display:inline-block;vertical-align:top;width:100%;">
                                <table role="presentation" style="vertical-align:top;" width="100%" cellspacing="0"
                                    cellpadding="0" border="0">
                                    <tbody>
                                        <tr>
                                            <td style="font-size:0px;padding:10px 25px;word-break:break-word;"
                                                align="left">
                                                <div
                                                    style="font-family:Montserrat, Helvetica, Arial, sans-serif;font-size:18px;font-weight:bold;line-height:24px;text-align:left;color:#dddddd;">
                                                    <h3
                                                        style="margin: 0; font-size: 22px; line-height: 26px; font-weight: 600; font-family: 'Inknut Antiqua', Helvetica, Arial, sans-serif;">
                                                        This week in gaming:</h3>
                                                </div>
                                            </td>
                                        </tr>
                                    </tbody>
                                </table>
                            </div>
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>
        <div style="margin:0px auto;max-width:600px;">
            <table role="presentation" style="width:100%;" cellspacing="0" cellpadding="0" border="0" align="center">
                <tbody>
                    <tr>
                        <td style="direction:ltr;font-size:0px;padding:0;text-align:center;">
                            <div class="mj-column-per-100 mj-outlook-group-fix"
                                style="font-size:0px;text-align:left;direction:ltr;display:inline-block;vertical-align:top;width:100%;">
                                <table role="presentation" style="vertical-align:top;" width="100%" cellspacing="0"
                                    cellpadding="0" border="0">
                                    <tbody>
                                        <tr>
                                            <td style="font-size:0px;padding:10px 25px;word-break:break-word;"
                                                align="left">
                                                <div
                                                    style="font-family:Montserrat, Helvetica, Arial, sans-serif;font-size:18px;font-weight:bold;line-height:24px;text-align:left;color:#dddddd;">
                                                    <h2
                                                        style="margin: 0; font-weight: 600; font-family: 'Inknut Antiqua', Helvetica, Arial, sans-serif; font-size: 24px; line-height: 30px;">
                                                        {gamingTitle}
                                                    </h2>
                                                </div>
                                            </td>
                                        </tr>
                                        <tr>
                                            <td style="font-size:0px;padding:10px 25px;word-break:break-word;"
                                                align="left">
                                                <div
                                                    style="font-family:Montserrat, Helvetica, Arial, sans-serif;font-size:18px;font-weight:400;line-height:24px;text-align:left;color:#dddddd;">
                                                    <img width="600px" height="auto"
                                                        src="{gamingImage}"
                                                        alt="Article Image">
                                                    <p style="margin: 0;white-space: pre-line;">
                                                        {gamingDescription}
                                                    </p>
                                                </div>
                                            </td>
                                        </tr>
                                        <tr>
                                            <td vertical-align="middle"
                                                style="font-size:0px;padding:10px 25px;word-break:break-word;"
                                                align="left">
                                                <table role="presentation"
                                                    style="border-collapse:separate;line-height:100%;" cellspacing="0"
                                                    cellpadding="0" border="0">
                                                    <tbody>
                                                        <tr>
                                                            <td role="presentation"
                                                                style="border:none;border-radius:3px;cursor:auto;mso-padding-alt:10px 25px;background:#ffffff;"
                                                                valign="middle" bgcolor="#ffffff" align="center">
                                                                <a href="{gamingLink}"
                                                                    style="display: inline-block; background: #ffffff; color: #000000; font-family: Montserrat, Helvetica, Arial, sans-serif; font-size: 14px; font-weight: normal; line-height: 30px; margin: 0; text-decoration: none; text-transform: none; padding: 10px 25px; mso-padding-alt: 0px; border-radius: 3px;"
                                                                    target="_blank">
                                                                    <strong>Read more</strong>
                                                                </a>
                                                            </td>
                                                        </tr>
                                                    </tbody>
                                                </table>
                                            </td>
                                        </tr>
                                    </tbody>
                                </table>
                            </div>
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>

        <div style="margin:0px auto;max-width:600px;">
            <table role="presentation" style="width:100%;" cellspacing="0" cellpadding="0" border="0" align="center">
                <tbody>
                    <tr>
                        <td style="direction:ltr;font-size:0px;padding:20px 0;text-align:center;">
                            <div class="mj-column-per-100 mj-outlook-group-fix"
                                style="font-size:0px;text-align:left;direction:ltr;display:inline-block;vertical-align:top;width:100%;">
                                <table role="presentation" style="vertical-align:top;" width="100%" cellspacing="0"
                                    cellpadding="0" border="0">
                                    <tbody>
                                        <tr>
                                            <td style="font-size:0px;padding:10px 25px;word-break:break-word;"
                                                align="left">
                                                <div
                                                    style="font-family:Montserrat, Helvetica, Arial, sans-serif;font-size:18px;font-weight:bold;line-height:24px;text-align:left;color:#dddddd;">
                                                    <h3
                                                        style="margin: 0; font-size: 22px; line-height: 26px; font-weight: 600; font-family: 'Inknut Antiqua', Helvetica, Arial, sans-serif;">
                                                        This week in tech:</h3>
                                                </div>
                                            </td>
                                        </tr>
                                    </tbody>
                                </table>
                            </div>
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>


      <div style="margin:0px auto;max-width:600px;">
        <table role="presentation" style="width:100%;" cellspacing="0" cellpadding="0" border="0" align="center">
            <tbody>
                <tr>
                    <td style="direction:ltr;font-size:0px;padding:0;text-align:center;">
                        <div class="mj-column-per-100 mj-outlook-group-fix"
                            style="font-size:0px;text-align:left;direction:ltr;display:inline-block;vertical-align:top;width:100%;">
                            <table role="presentation" style="vertical-align:top;" width="100%" cellspacing="0"
                                cellpadding="0" border="0">
                                <tbody>
                                    <tr>
                                        <td style="font-size:0px;padding:10px 25px;word-break:break-word;"
                                            align="left">
                                            <div
                                                style="font-family:Montserrat, Helvetica, Arial, sans-serif;font-size:18px;font-weight:bold;line-height:24px;text-align:left;color:#dddddd;">
                                                <h2
                                                    style="margin: 0; font-weight: 600; font-family: 'Inknut Antiqua', Helvetica, Arial, sans-serif; font-size: 24px; line-height: 30px;">
                                                    {techTitle}
                                                </h2>
                                            </div>
                                        </td>
                                    </tr>
                                    <tr>
                                        <td style="font-size:0px;padding:10px 25px;word-break:break-word;"
                                            align="left">
                                            <div
                                                style="font-family:Montserrat, Helvetica, Arial, sans-serif;font-size:18px;font-weight:400;line-height:24px;text-align:left;color:#dddddd;">
                                                <img width="600px" height="auto"
                                                        src="{techImage}"
                                                        alt="Article Image">
                                                <p style="margin: 0;white-space: pre-line;">
                                                    {techDescription}
                                                </p>
                                            </div>
                                        </td>
                                    </tr>
                                    <tr>
                                        <td vertical-align="middle"
                                            style="font-size:0px;padding:10px 25px;word-break:break-word;"
                                            align="left">
                                            <table role="presentation"
                                                style="border-collapse:separate;line-height:100%;" cellspacing="0"
                                                cellpadding="0" border="0">
                                                <tbody>
                                                    <tr>
                                                        <td role="presentation"
                                                            style="border:none;border-radius:3px;cursor:auto;mso-padding-alt:10px 25px;background:#ffffff;"
                                                            valign="middle" bgcolor="#ffffff" align="center">
                                                            <a href="{techLink}"
                                                                style="display: inline-block; background: #ffffff; color: #000000; font-family: Montserrat, Helvetica, Arial, sans-serif; font-size: 14px; font-weight: normal; line-height: 30px; margin: 0; text-decoration: none; text-transform: none; padding: 10px 25px; mso-padding-alt: 0px; border-radius: 3px;"
                                                                target="_blank">
                                                                <strong>Read more</strong>
                                                            </a>
                                                        </td>
                                                    </tr>
                                                </tbody>
                                            </table>
                                        </td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                    </td>
                </tr>
            </tbody>
        </table>
    </div>


    <!--CONTACT-->>
        <div style="margin:0px auto;max-width:600px;">
            <table role="presentation" style="width:100%;" cellspacing="0" cellpadding="0" border="0" align="center">
                <tbody>
                    <tr>
                        <td style="direction:ltr;font-size:0px;padding:20px 0;text-align:center;">
                            <div class="mj-column-per-100 mj-outlook-group-fix"
                                style="font-size:0px;text-align:left;direction:ltr;display:inline-block;vertical-align:top;width:100%;">
                                <table role="presentation" style="vertical-align:top;" width="100%" cellspacing="0"
                                    cellpadding="0" border="0">
                                    <tbody>
                                        <tr>
                                            <td style="font-size:0px;padding:10px 25px;word-break:break-word;"
                                                align="left">
                                                <div
                                                    style="font-family:Montserrat, Helvetica, Arial, sans-serif;font-size:16px;font-weight:400;line-height:24px;text-align:left;color:#999999;">
                                                    <p style="margin: 0;">Have enquiries? Email us at <a href="mailto:netsoc@uccsocieties.ie"
                                                            style="color: #ffffff; text-decoration: underline; font-weight: bold;">netsoc@uccsocieties.ie</a>
                                                    </p>
                                                </div>
                                            </td>
                                        </tr>
                                    </tbody>
                                </table>
                            </div>
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>

        <!--FOOTER-->
        <table role="presentation" style="background:#000000;background-color:#000000;width:100%;" cellspacing="0"
            cellpadding="0" border="0" align="center">
            <tbody>
                <tr>
                    <td>
                        <div style="margin:0px auto;max-width:600px;">
                            <table role="presentation" style="width:100%;" cellspacing="0" cellpadding="0" border="0"
                                align="center">
                                <tbody>
                                    <tr>
                                        <td style="direction:ltr;font-size:0px;padding:20px 0;text-align:center;">
                                            <div class="mj-column-per-100 mj-outlook-group-fix"
                                                style="font-size:0px;text-align:left;direction:ltr;display:inline-block;vertical-align:top;width:100%;">
                                                <table role="presentation" style="vertical-align:top;" width="100%"
                                                    cellspacing="0" cellpadding="0" border="0">
                                                    <tbody>
                                                        <tr>
                                                            <td style="font-size:0px;padding:10px 25px;word-break:break-word;"
                                                                align="center">
                                                                <table role="presentation"
                                                                    style="float:none;display:inline-table;"
                                                                    cellspacing="0" cellpadding="0" border="0"
                                                                    align="center">
                                                                    <tbody>
                                                                        <tr>
                                                                            <td style="padding:4px;">
                                                                                <table role="presentation"
                                                                                    style="border-radius:3px;width:24px;"
                                                                                    cellspacing="0" cellpadding="0"
                                                                                    border="0">
                                                                                    <tbody>
                                                                                        <tr>
                                                                                            <td
                                                                                                style="font-size:0;height:24px;vertical-align:middle;width:24px;">
                                                                                                <a href="https://twitter.com/uccnetsoc"
                                                                                                    target="_blank"
                                                                                                    style="color: #ffffff; text-decoration: underline; font-weight: bold;">
                                                                                                    <img alt="twitter-logo"
                                                                                                        src="https://codedmails.com/images/social/light/twitter-logo-transparent-light.png"
                                                                                                        style="border-radius:3px;display:block;"
                                                                                                        width="24"
                                                                                                        height="24" />
                                                                                                </a>
                                                                                            </td>
                                                                                        </tr>
                                                                                    </tbody>
                                                                                </table>
                                                                            </td>
                                                                        </tr>
                                                                    </tbody>
                                                                </table>
                                                                <table role="presentation"
                                                                    style="float:none;display:inline-table;"
                                                                    cellspacing="0" cellpadding="0" border="0"
                                                                    align="center">
                                                                    <tbody>
                                                                        <tr>
                                                                            <td style="padding:4px;">
                                                                                <table role="presentation"
                                                                                    style="border-radius:3px;width:24px;"
                                                                                    cellspacing="0" cellpadding="0"
                                                                                    border="0">
                                                                                    <tbody>
                                                                                        <tr>
                                                                                            <td
                                                                                                style="font-size:0;height:24px;vertical-align:middle;width:24px;">
                                                                                                <a href="https://www.instagram.com/uccnetsoc/"
                                                                                                    target="_blank"
                                                                                                    style="color: #ffffff; text-decoration: underline; font-weight: bold;">
                                                                                                    <img alt="instagram-logo"
                                                                                                        src="https://codedmails.com/images/social/light/instagram-logo-transparent-light.png"
                                                                                                        style="border-radius:3px;display:block;"
                                                                                                        width="24"
                                                                                                        height="24" />
                                                                                                </a>
                                                                                            </td>
                                                                                        </tr>
                                                                                    </tbody>
                                                                                </table>
                                                                            </td>
                                                                        </tr>
                                                                    </tbody>
                                                                </table>
                                                            </td>
                                                        </tr>
                                                        <tr>
                                                            <td style="font-size:0px;word-break:break-word;">
                                                                <div style="height:20px;">   </div>
                                                            </td>
                                                        </tr>
                                                        <tr>
                                                            <td style="font-size:0px;padding:10px 25px;word-break:break-word;"
                                                                align="center">
                                                                <div
                                                                    style="font-family:Montserrat, Helvetica, Arial, sans-serif;font-size:16px;font-weight:400;line-height:24px;text-align:center;color:#999999;"
                                                                >
                                                                    To unsubscribe, please visit the <a style="color: #ffffff" href="https://candsportal.ucc.ie/mailinglistunsubscribe.php?list=wistem-announce@portalmail.ucc.ie&email=$user_email">this link</a>
                                                                    and choose netsoc-announce@portalmail.ucc.ie. If this does not work, please let us know at <a style="color: #ffffff" href="mailto:netsoc@uccsocieties.ie">netsoc@uccsocieties.ie</a>.
                                                                </div>
                                                            </td>
                                                        </tr>
                                                    </tbody>
                                                </table>
                                            </div>
                                        </td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                    </td>
                </tr>
            </tbody>
        </table>


</body>

</html>
'''

    return head