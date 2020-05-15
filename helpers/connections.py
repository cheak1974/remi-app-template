import datetime
import remi
import core.globals

connected_clients = {}                              # Dict with key=session id of App Instance and value=ws_client.client_address of App Instance
connected_clients['number'] = 0                     # Special Dict Field for amount of active connections
client_route_url_to_view = {}                       # Dict to store URL extensions related to session. This is used to switch a view based on url


def handle_connections(AppInst=None):
    # Take care of the connection. It is only alive if the websocket still is active.
    # Check, if there is a new websocket connection for this App session (= Instance)

    if AppInst.connection_established == False and len(AppInst.websockets) == 1:
        for session_id, app_inst in remi.server.clients.items():
            if session_id == AppInst.session:
                for ws_client in app_inst.websockets:

                    if core.globals.config['is_behind_proxy'] == True:          # If you are behind a proxy use the X-Forwarded-For Header instead of ws host info

                        headerlines = str(ws_client.headers).split('\n')         # Split header information along \n

                        for header in headerlines:
                            if header.find('X-Forwarded-For') >= 0:         # Header used by reverse Proxies to forward original host IP
                                host = header.split(':')
                                AppInst.logger.info(f'New Session with ID <{AppInst.session}> from host {host[1].strip()}')
                                connected_clients[AppInst.session] = host[1].strip()

                    else:
                        AppInst.logger.info(f'New Session with ID <{AppInst.session}> from host {ws_client.client_address}')    # Host Information for direct connection
                        connected_clients[AppInst.session] = ws_client.client_address

                    AppInst.logger.info(f'Session <{AppInst.session}> host headers: {ws_client.headers}')
                    connected_clients['number'] = connected_clients['number'] + 1
                    AppInst.logger.info(f'Connected clients ({connected_clients["number"]} in total): {connected_clients}')

        AppInst.connect_time = datetime.datetime.now()
        AppInst.connection_established = True                   # Set Flag. This can be used by other threads as end signal.

    # Check, if the websocket connection is still alive. REMI removes the Websocket from the List if dead.
    if len(remi.server.clients[AppInst.session].websockets) == 0 and AppInst.connection_established == True:
        AppInst.disconnect_time = datetime.datetime.now()  # Store the disconnect time
        connection_duration = f'{(AppInst.disconnect_time - AppInst.connect_time).seconds} sec'
        AppInst.logger.info(f'Session <{AppInst.session}> from host {connected_clients[AppInst.session]} has disconnected. Connection duration: {connection_duration}')
        AppInst.connection_established = False  # Set Flag. This can be used by other threads as end signal.

        del connected_clients[AppInst.session]
        connected_clients['number'] = connected_clients['number'] - 1
        AppInst.logger.info(f'Still connected clients: {connected_clients}')
