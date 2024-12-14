from controllers import ElectionController
from gui import MainApplication
from storage import load_data, save_data


def main():
    controller = ElectionController()
    # Initialize candidates here or load from file
    controller.add_candidate('Corey')
    controller.add_candidate('Collin')
    controller.add_candidate('Issac')

    load_data(controller)  # Load data if available

    app = MainApplication(controller)
    app.protocol("WM_DELETE_WINDOW", lambda: on_close(app, controller))  # Handle window close event
    app.mainloop()


def on_close(app: MainApplication, controller: ElectionController):
    save_data(controller)  # Save data on close
    app.destroy()


if __name__ == '__main__':
    main()
